#!/usr/bin/env python

import re
import gspread
from gspread.utils import *
from gspread.exceptions import *
from gspread_formatting import *

from ggle.google_worksheet import GoogleWorksheet

from helper.utils import *
from helper.logger import *
from helper.data import *

from pprint import pprint


''' Google sheet wrapper
'''
class GoogleSheet(object):

    ''' constructor
    '''
    def __init__(self, google_service, gspread_sheet, wait_for, try_for):
        self.service = google_service
        self.gspread_sheet = gspread_sheet
        self.id = self.gspread_sheet.id
        self.title = self.gspread_sheet.title
        self.wait_for = wait_for
        self.try_for = try_for

        self.worksheets = self.gspread_sheet.worksheets()



    ''' given a list of names and exlusion list, get the worksheets with matching names exluding worksheets with matching names in the exlusion list
    '''
    def matching_worksheet_names(self, worksheet_names, worksheet_names_excluded, nesting_level=0):
        all_worksheet_names = self.list_worksheets()
        included_worksheets = []
        for ws_name in all_worksheet_names:
            # if it matches any in the inclusion list, include it
            for inclusion_pattern in worksheet_names:
                m = re.match(inclusion_pattern, ws_name)
                if m:
                    included_worksheets.append(ws_name)
                    continue

        excluded_worksheets = []
        for ws_name in included_worksheets:
            # if it matches any in the exlusion list, include it
            for exclusion_pattern in worksheet_names_excluded:
                m = re.match(exclusion_pattern, ws_name)
                if m:
                    excluded_worksheets.append(ws_name)
                    continue
            
        # finally the matching list
        matching_worksheets = [x for x in included_worksheets if x not in excluded_worksheets]

        return matching_worksheets


    ''' get range values
    '''
    def get_range_values(self, range_spec, nesting_level=0, **kwargs):
        params = {'majorDimension': 'ROWS'}
        params.update(kwargs)
        return self.gspread_sheet.values_get(range_spec, params=params)



    ''' get range values in batch
    '''
    def get_range_values_in_batch(self, range_spec, requester='', nesting_level=0, **kwargs):
        params = {'majorDimension': 'ROWS'}
        params.update(kwargs)

        for try_count in range(1, self.try_for+1):
            try:
                values = self.gspread_sheet.values_batch_get(range_spec, params=params)
                # print(range_spec, values)
                return values
            except Exception as e:
                print(e)
                if try_count < self.try_for:
                    warn(f"[{requester}] batch-get failed in [{try_count}/{self.try_for}] try, trying again in {self.wait_for} seconds", nesting_level=nesting_level)
                    time.sleep(self.wait_for)
                else:
                    warn(f"[{requester}] batch-get failed in [{try_count}/{self.try_for}] try", nesting_level=nesting_level)

        return None



    ''' get conditional formats
    '''
    def get_conditional_formats(self, nesting_level=0):
        fields = 'sheets(properties.title,conditionalFormats)'
        # ranges = [f"'{worksheet_name}'!{range_spec}"]
        conditional_formats = {}
        for try_count in range(1, self.try_for+1):
            try:
                request = self.service.gsheet_service.spreadsheets().get(spreadsheetId=self.id, includeGridData=True, fields=fields)
                response = request.execute()
                # debug(f"get conditional formats passed in [{try_count}] try", nesting_level=nesting_level)
                if 'sheets' in response:
                    for sheet in response['sheets']:
                        if 'conditionalFormats' in sheet:
                            conditional_formats[sheet['properties']['title']] = sheet['conditionalFormats']

                return conditional_formats

            except Exception as e:
                print(e)
                if try_count < self.try_for:
                    warn(f"get conditional formats failed in [{try_count}] try, trying again in {self.wait_for} seconds", nesting_level=nesting_level)
                    time.sleep(self.wait_for)
                else:
                    warn(f"get conditional formats failed in [{try_count}] try", nesting_level=nesting_level)

        return conditional_formats



    ''' get column sizes
    '''
    def get_column_sizes(self, nesting_level=0):
        fields = 'sheets(properties.title,data(columnMetadata(pixelSize)))'
        for try_count in range(1, self.try_for+1):
            try:
                request = self.service.gsheet_service.spreadsheets().get(spreadsheetId=self.id, includeGridData=True, fields=fields)
                response = request.execute()
                # debug(f"get worksheet passed in [{try_count}] try", nesting_level=nesting_level)
                column_sizes = {sheet['properties']['title']: [ pixel_size['pixelSize'] for pixel_size in sheet['data'][0]['columnMetadata'] ] for sheet in response['sheets']}
                return column_sizes
            except Exception as e:
                print(e)
                if try_count < self.try_for:
                    warn(f"get worksheet failed in [{try_count}] try, trying again in {self.wait_for} seconds", nesting_level=nesting_level)
                    time.sleep(self.wait_for)
                else:
                    warn(f"get worksheet failed in [{try_count}] try", nesting_level=nesting_level)

        return None



    ''' copy worksheet to another gsheet
    '''
    def copy_worksheet_to_gsheet(self, destination_gsheet, worksheet_name_to_copy, nesting_level=0):
        # if destination already has a worksheet of the same name, do not do anything
        destintion_worksheet = destination_gsheet.worksheet_by_name(worksheet_name_to_copy, suppress_log=True, nesting_level=nesting_level+1)
        if destintion_worksheet:
            warn(f"worksheet [{worksheet_name_to_copy}] already exists in [{destination_gsheet.title}]")
            return

        worksheet_to_copy = self.worksheet_by_name(worksheet_name_to_copy, nesting_level=nesting_level+1)
        if worksheet_to_copy:
            worksheet_to_copy.copy_worksheet_to_gsheet(destination_gsheet)



    ''' update spreadsheet in batch
    '''
    def update_in_batch(self, values, requests, requester='', nesting_level=0):
        info(f"batch-updating [{len(values)}] values and [{len(requests)}] formats", nesting_level=nesting_level)
        value_results, request_results = [], []
        if len(values):
            value_results = self.update_values_in_batch(value_list=values, requester=requester, nesting_level=nesting_level+1)

        if len(requests):
            request_results = self.update_formats_in_batch(request_list=requests, requester=requester, nesting_level=nesting_level+1)

        info(f"batch-updated  [{len(values)}] values and [{len(requests)}] formats", nesting_level=nesting_level)

        return value_results, request_results



    ''' update spreadsheet formats in batch
    '''
    def update_formats_in_batch(self, request_list, requester='', nesting_level=0):
        for try_count in range(1, self.try_for+1):
            try:
                response = self.gspread_sheet.batch_update(body={'requests': request_list})
                # debug(f"[{requester}] batch-update passed in [{try_count}] try", nesting_level=nesting_level)
                return response
            except Exception as e:
                print(e)
                if try_count < self.try_for:
                    warn(f"[{requester}] batch-update failed in [{try_count}/{self.try_for}] try, trying again in {self.wait_for} seconds", nesting_level=nesting_level)
                    time.sleep(self.wait_for)
                else:
                    warn(f"[{requester}] batch-update failed in [{try_count}/{self.try_for}] try", nesting_level=nesting_level)



    ''' update spreadsheet values in batch
    '''
    def update_values_in_batch(self, value_list, requester='', nesting_level=0):
        batch_update_values_request_body = {
                'value_input_option': 'USER_ENTERED',
                'data': value_list,
            }

        for try_count in range(1, self.try_for+1):
            try:
                request = self.service.gsheet_service.spreadsheets().values().batchUpdate(spreadsheetId=self.id, body=batch_update_values_request_body)
                response = request.execute()
                # debug(f"[{requester}] value-update passed in [{try_count}] try", nesting_level=nesting_level)
                return response
            except Exception as e:
                print(e)
                if try_count < self.try_for:
                    warn(f"[{requester}] value-update failed in [{try_count}] try, trying again in {self.wait_for} seconds", nesting_level=nesting_level)
                    time.sleep(self.wait_for)
                else:
                    warn(f"[{requester}] value-update failed in [{try_count}] try", nesting_level=nesting_level)



    ''' share a gsheet
    '''
    def share(self, email, perm_type, role, nesting_level=0):
        self.gspread_sheet.share(email_address=email, perm_type=perm_type, role=role, notify=False)



    ''' get worksheet by name
    '''
    def worksheet_by_name(self, worksheet_name, suppress_log=True, nesting_level=0):
        for ws in self.worksheets:
            if ws.title == worksheet_name:
                if not suppress_log:
                    debug(f"worksheet [{worksheet_name:<40}] found", nesting_level=nesting_level)

                return GoogleWorksheet(google_service=self.service, gspread_worksheet=ws, gsheet=self, wait_for=self.wait_for, try_for=self.try_for)

        if not suppress_log:
            error(f"worksheet [{worksheet_name:<40}] not found", nesting_level=nesting_level)



    ''' returns a dict {worksheet_name, worksheet_id}
    '''
    def worksheets_as_dict(self, nesting_level=0):
        worksheets_dict = { gspread_worksheet.title : gspread_worksheet.id for gspread_worksheet in self.worksheets }
        return worksheets_dict



    ''' list worksheets of the gsheet
    '''
    def list_worksheets(self, nesting_level=0):
        return [ ws.title for ws in self.worksheets ]



    ''' order the worksheets of the gsheet alphabetically
    '''
    def order_worksheets(self, nesting_level=0):
        info(f"ordering worksheets for {self.gspread_sheet.title}", nesting_level=nesting_level)
        reordered_worksheets = sorted(self.worksheets, key=lambda x: x.title, reverse=False)
        self.gspread_sheet.reorder_worksheets(reordered_worksheets)
        info(f"ordered  worksheets for {self.title}", nesting_level=nesting_level)



    ''' rename a worksheet
    '''
    def rename_worksheet(self, worksheet_name, new_worksheet_name, check_condition=False, conditions=[], nesting_level=0):
        worksheet_to_rename = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
        if worksheet_to_rename:
            condition_satisfied = worksheet_to_rename.check_condition(check_condition=check_condition, conditions=conditions, nesting_level=nesting_level+1)
            if condition_satisfied:
                worksheet_to_rename.rename_worksheet(new_worksheet_name, nesting_level=nesting_level+1)



    ''' remove a worksheet
    '''
    def remove_worksheets(self, worksheet_names, check_condition=False, conditions=[], nesting_level=0):
        for worksheet_name in worksheet_names:
            worksheet_to_remove = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet_to_remove:
                condition_satisfied = worksheet_to_remove.check_condition(check_condition=check_condition, conditions=conditions, nesting_level=nesting_level+1)
                if condition_satisfied:
                    try:
                        info(f"removing worksheet {worksheet_name}", nesting_level=nesting_level)
                        self.gspread_sheet.del_worksheet(worksheet_to_remove)
                        info(f"removed  worksheet {worksheet_name}", nesting_level=nesting_level)

                    except:
                        warn(f"worksheet {worksheet_name} could not be removed", nesting_level=nesting_level)



    ''' bulk create multiple worksheets by duplicating a given worksheet
    '''
    def duplicate_worksheet(self, worksheet_names, worksheet_name_to_duplicate, check_condition=False, conditions=[], nesting_level=0):
        worksheet_to_duplicate = self.worksheet_by_name(worksheet_name_to_duplicate, nesting_level=nesting_level+1)
        if worksheet_to_duplicate:
            requests = worksheet_to_duplicate.duplicate_worksheet_requests(new_worksheet_names=worksheet_names, nesting_level=nesting_level+1)
            self.update_in_batch(values=[], requests=requests, requester='duplicate_worksheet', nesting_level=nesting_level+1)



    ''' link cells of a worksheet to drive-file/worksheet based type
        type is valid only if the range has two columns
        if the range has only one column default to worksheet link
    '''
    def link_cells_based_on_type(self, worksheet_name, range_specs_for_cells_to_link, nesting_level=0):
        worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
        if worksheet_to_work_on:
            worksheets_dict = self.worksheets_as_dict()
            values, requests = worksheet_to_work_on.cell_link_based_on_type_requests(range_specs_for_cells_to_link=range_specs_for_cells_to_link, worksheets_dict=worksheets_dict)
            self.update_in_batch(values=values, requests=requests, requester='link_cells_based_on_type', nesting_level=nesting_level+1)



    ''' link cells of a worksheet to drive files where cells values are names of drive files
        link_cells_based_on_type is preferred
    '''
    def link_cells_to_drive_files(self, worksheet_name, range_specs_for_cells_to_link, nesting_level=0):
        worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
        if worksheet_to_work_on:
            values, requests = worksheet_to_work_on.cell_to_drive_file_link_requests(range_specs_for_cells_to_link=range_specs_for_cells_to_link, nesting_level=nesting_level)
            self.update_in_batch(values=values, requests=requests, requester='link_cells_to_drive_files', nesting_level=nesting_level+1)



    ''' link cells of a worksheet to worksheets where cells values are names of worksheets
        link_cells_based_on_type is preferred
    '''
    def link_cells_to_worksheet(self, worksheet_name, range_specs_for_cells_to_link, nesting_level=0):
        worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
        if worksheet_to_work_on:
            worksheets_dict = self.worksheets_as_dict()
            values, requests = worksheet_to_work_on.cell_to_worksheet_link_requests(range_specs_for_cells_to_link=range_specs_for_cells_to_link, worksheets_dict=worksheets_dict, nesting_level=nesting_level+1)
            self.update_in_batch(values=values, requests=requests, requester='link_cells_to_worksheet', nesting_level=nesting_level+1)



    ''' find and replace in worksheets
    '''
    def find_and_replace(self, worksheet_names, find_replace_patterns=[], check_condition=False, conditions=[], nesting_level=0):
        requests = []
        for worksheet_name in worksheet_names:
            info(f"searching [{len(find_replace_patterns)}] patterns in  [{worksheet_name}]", nesting_level=nesting_level)
            worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet_to_work_on:
                reqs = worksheet_to_work_on.find_and_replace_requests(find_replace_patterns=find_replace_patterns)
                info(f"found     [{len(reqs)}] patterns in  [{worksheet_name}]", nesting_level=nesting_level)
                requests = requests + reqs

        result = self.update_in_batch(values=[], requests=requests, requester='find_and_replace', nesting_level=nesting_level+1)
        return result



    ''' clear data validations for a range
    '''
    def clear_data_validations(self, worksheet_names, range_spec, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        for worksheet_name in worksheet_names:
            worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet_to_work_on:
                reqs = worksheet_to_work_on.data_validation_clear_requests(range_spec=range_spec)
                requests = requests + reqs

        self.update_in_batch(values=[], requests=requests, requester='clear_data_validations', nesting_level=nesting_level+1)



    ''' get and clear conditional formats
    '''
    def clear_conditional_formats(self, worksheet_names, check_condition=False, conditions=[], nesting_level=0):
        conditional_formats = self.get_conditional_formats()
        requests = []
        for worksheet_name in worksheet_names:
            if worksheet_name not in conditional_formats:
                debug(f"No conditional format exists for [{worksheet_name}]")
                continue

            worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet_to_work_on:
                number_of_rules = len(conditional_formats[worksheet_name])
                reqs = worksheet_to_work_on.clear_conditional_formats_requests(number_of_rules=number_of_rules)
                requests = requests + reqs

        self.update_in_batch(values=[], requests=requests, requester='clear_conditional_formats', nesting_level=nesting_level+1)



    ''' work on a (list of) worksheet's range of work specs for value and format updates
    '''
    def work_on_ranges(self, worksheet_names, work_specs={}, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        values = []
        worksheets_dict = self.worksheets_as_dict()
        for worksheet_name in worksheet_names:
            # info(f"working on .. [{len(work_specs.keys())}] ranges on [{worksheet_name}]", nesting_level=nesting_level)
            worksheet_to_work_on = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet_to_work_on:
                condition_satisfied = worksheet_to_work_on.check_condition(check_condition=check_condition, conditions=conditions, nesting_level=nesting_level+1)
                if condition_satisfied:
                    vals, reqs = worksheet_to_work_on.range_work_requests(range_work_specs=work_specs, worksheets_dict=worksheets_dict, nesting_level=nesting_level+1)
                    values = values + vals
                    requests = requests + reqs

        self.update_in_batch(values=values, requests=requests, requester='work_on_ranges', nesting_level=nesting_level+1)



    ''' put column size in pixels in row 1 for all columns except A
    '''
    def column_pixels_in_row(self, worksheet_names, row_to_update, nesting_level=0):
        values, requests = [], []
        column_sizes = self.get_column_sizes()
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet:
                vals, reqs = worksheet.column_pixels_in_row_requests(column_sizes=column_sizes, row_to_update=row_to_update)
                values = values + vals
                requests = requests + reqs

        self.update_in_batch(values=values, requests=requests, requester='column_pixels_in_row', nesting_level=nesting_level+1)



    ''' resize columns with the size mentioned in pixel number in row 1 for that column
    '''
    def resize_columns_from_values_in_row(self, worksheet_names, row_to_consult, nesting_level=0):
        values, requests = [], []
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet:
                vals, reqs = worksheet.resize_columns_from_values_in_row_requests(row_to_consult=row_to_consult)
                values = values + vals
                requests = requests + reqs

        self.update_in_batch(values=values, requests=requests, requester='resize_columns_from_values_in_row', nesting_level=nesting_level+1)



    ''' move column
        worksheet_name: worksheet name in which to order columns
        row_to_consult: worksheet row where the values are and based on what to order the columns
        order_by_values: a list of values based on which ordering to be done by matching them with the values in the specified row
    ''' 
    def move_column(self, worksheet_name, move_from, move_to, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        worksheet = self.worksheet_by_name(worksheet_name=worksheet_name, nesting_level=nesting_level+1)
        if worksheet:
            condition_satisfied = worksheet.check_condition(check_condition=check_condition, conditions=conditions, nesting_level=nesting_level+1)
            if condition_satisfied:
                move_from_index = LETTER_TO_COLUMN[move_from] - 1
                move_to_index = LETTER_TO_COLUMN[move_to]
                if worksheet.num_cols() < move_from_index:
                    warn(f"worksheet [{worksheet.gspread_worksheet.title:<40}] does not have column [{move_from}]", nesting_level=nesting_level)
                    return

                if worksheet.num_cols() < move_to_index:
                    warn(f"worksheet [{worksheet.gspread_worksheet.title:<40}] does not have column [{move_to}]", nesting_level=nesting_level)
                    return
                
                trace(f"worksheet [{worksheet.gspread_worksheet.title:<40}] moving column [{move_from}] to [{move_to}]", nesting_level=nesting_level)
                requests = worksheet.dimension_move_requests(dimension='COLUMNS', from_index=move_from_index, to_index=move_to_index, nesting_level=nesting_level+1)

                self.update_in_batch(values=[], requests=requests, requester='move_column', nesting_level=nesting_level+1)



    ''' order columns
        worksheet_name: worksheet name in which to order columns
        row_to_consult: worksheet row where the values are and based on what to order the columns
        order_by_values: a list of values based on which ordering to be done by matching them with the values in the specified row
    ''' 
    def order_columns(self, worksheet_name, row_to_consult, order_by_values, nesting_level=0):
        requests = []
        worksheet = self.worksheet_by_name(worksheet_name=worksheet_name, nesting_level=nesting_level+1)
        if worksheet:
            # get values from row_to_consult
            row_values = worksheet.get_row_values(row_num=row_to_consult, nesting_level=nesting_level+1)

            # provided values may have lables which are not in the row, we should be removing them from provided values
            valid_target_order = [label for label in order_by_values if label in row_values]

            # build the move requests
            for target_idx, label in enumerate(valid_target_order):
                try:
                    current_idx = row_values.index(label)
                    if current_idx != target_idx:
                        current_col = COLUMN_TO_LETTER[current_idx]
                        target_col = COLUMN_TO_LETTER[target_idx]
                        trace(f"column [{current_col}]:[{label}] will be moved to column [{target_col}]", nesting_level=nesting_level+1)
                        requests.append(worksheet.dimension_move_requests(dimension='COLUMNS', from_index=current_idx, to_index=target_idx, nesting_level=nesting_level+1))

                        # Update our local list to reflect the move so the next loop is accurate
                        col = row_values.pop(current_idx)
                        row_values.insert(target_idx, col)

                except ValueError:
                    warn(f"worksheet [{worksheet.gspread_worksheet.title:<40}] no column found with label '{label}' in Row {row_to_consult}", nesting_level=nesting_level)
            
            self.update_in_batch(values=[], requests=requests, requester='order_columns', nesting_level=nesting_level+1)



    ''' remove columns
        worksheet_name: worksheet name from which to remove columns
        cols_to_remove_from: column letter from where to start removal
        cols_to_remove_to: column letter upto where to remove
        check_condition: whether to check any condition for the removal. all conditions must be satisfied
        conditions: if check_condition, a list of condition dicts
            cell_a1: cell on which the condition is to be checked
            value_is: cell_a1 value that must be satisfied for this condition to be satisfied
    '''
    def remove_columns(self, worksheet_name, cols_to_remove_from, cols_to_remove_to, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        worksheet = self.worksheet_by_name(worksheet_name=worksheet_name, nesting_level=nesting_level+1)
        if worksheet:
            # check if the worksheet column count is valid for the operation
            if worksheet.num_cols() >= LETTER_TO_COLUMN[cols_to_remove_from]:
                condition_satisfied = worksheet.check_condition(check_condition=check_condition, conditions=conditions, nesting_level=nesting_level+1)
                if condition_satisfied:
                    requests = worksheet.remove_columns_requests(cols_to_remove_from=cols_to_remove_from, cols_to_remove_to=cols_to_remove_to)

                    self.update_in_batch(values=[], requests=requests, requester='remove_columns', nesting_level=nesting_level+1)
    
            else:
                warn(f"worksheet [{worksheet.gspread_worksheet.title:<40}] does not have column [{cols_to_remove_from}]", nesting_level=nesting_level)


    ''' report dimesnions
    '''
    def report_dimensions(self, worksheet_names, nesting_level=0):
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name, suppress_log=False, nesting_level=nesting_level+1)
            num_rows, num_cols = worksheet.number_of_dimesnions()
            if worksheet:
                info(f"[{num_cols}] cols in [{worksheet_name:40}] worksheet for gsheet [{self.title}]", nesting_level=nesting_level)
                info(f"[{num_rows}] rows in [{worksheet_name:40}] worksheet for gsheet [{self.title}]", nesting_level=nesting_level)



    ''' remove trailing blank rows from a worksheet
    '''
    def remove_trailing_blank_rows(self, worksheet_names, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name, nesting_level=nesting_level+1)
            if worksheet:
                reqs = worksheet.remove_trailing_blank_rows_requests(nesting_level=nesting_level+1)
                requests = requests + reqs

        self.update_in_batch(values=[], requests=requests, requester='remove_trailing_blank_rows', nesting_level=nesting_level+1)



    ''' number of rows and columns of a worksheet
    '''
    def number_of_dimesnions(self, worksheet_name, suppress_log=False, nesting_level=0):
        worksheet = self.worksheet_by_name(worksheet_name, suppress_log=suppress_log, nesting_level=nesting_level+1)
        if worksheet:
            return worksheet.number_of_dimesnions(nesting_level=nesting_level+1)
        else:
            return 0, 0



    ''' add rows in a worksheet
        rows will be added after rows_to_add_at
    '''
    def add_rows(self, worksheet_names, rows_to_add_at, rows_to_add, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name, suppress_log=False, nesting_level=nesting_level+1)
            if worksheet:
                reqs = worksheet.dimension_add_requests(rows_to_add_at=rows_to_add_at, rows_to_add=rows_to_add)
                requests = requests + reqs
        
        self.update_in_batch(values=[], requests=requests, requester='add_rows', nesting_level=nesting_level+1)



    ''' add column in a worksheet
        columns will be added after rows_to_add_at
    '''
    def add_columns(self, worksheet_names, cols_to_add_at, cols_to_add, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name, suppress_log=False, nesting_level=nesting_level+1)
            if worksheet:
                condition_satisfied = worksheet.check_condition(check_condition=check_condition, conditions=conditions, nesting_level=nesting_level+1)
                if condition_satisfied:
                    reqs = worksheet.dimension_add_requests(cols_to_add_at=cols_to_add_at, cols_to_add=cols_to_add)
                    requests = requests + reqs
        
        self.update_in_batch(values=[], requests=requests, requester='add_columns', nesting_level=nesting_level+1)



    ''' create review-notes conditional formatting
    '''
    def create_review_notes_conditional_formatting(self, worksheet_names, check_condition=False, conditions=[], nesting_level=0):
        requests = []
        for worksheet_name in worksheet_names:
            worksheet = self.worksheet_by_name(worksheet_name=worksheet_name, nesting_level=nesting_level+1)
            info(f"updating review-notes conditional formatting for worksheet {worksheet_name}", nesting_level=nesting_level)
            if worksheet:
                # Get number of columns
                num_cols = worksheet.num_cols()
                requests = requests + worksheet.conditional_formatting_for_review_notes_requests(num_cols=num_cols)

        # finally update in batch
        self.update_in_batch(values=[], requests=requests, requester='create_review_notes_conditional_formatting', nesting_level=nesting_level+1)



    ''' copy worksheets to another gsheet
    '''
    def copy_worksheets_to_other_gsheets(self, worksheet_names, destination_gsheet_names, nesting_level=0):
        for destination_gsheet_name in destination_gsheet_names:
            destination_gsheet = self.service.open(gsheet_name=destination_gsheet_name)
            if destination_gsheet:
                for worksheet_name in worksheet_names:
                    info(f"copying [{worksheet_name}] to gsheet [{destination_gsheet_name}]", nesting_level=nesting_level+1)
                    self.copy_worksheet_to_gsheet(destination_gsheet=destination_gsheet, worksheet_name_to_copy=worksheet_name)
            
            else:
                warn(f"destination gsheet [{destination_gsheet_name}] not found", nesting_level=nesting_level+1)



    ''' create worksheets according to spec defined in worksheet_defs
    '''
    def create_worksheets(self, worksheet_names, worksheet_defs, check_condition=False, conditions=[], nesting_level=0):
        worksheet_add_requests = []
        for worksheet_name in worksheet_names:
            if worksheet_name in worksheet_defs:
                info(f"creating worksheet {worksheet_name}", nesting_level=nesting_level)

                worksheet_add_requests = worksheet_add_requests + self.create_worksheet(worksheet_name=worksheet_name, worksheet_def=worksheet_defs[worksheet_name])

            else:
                warn(f"worksheet {worksheet_name} : structure not defined", nesting_level=nesting_level)

        # finally update in batch
        self.update_in_batch(values=[], requests=worksheet_add_requests, requester='create_worksheets', nesting_level=nesting_level+1)



    ''' create a worksheet according to spec defined in worksheet_def
    '''
    def create_worksheet(self, worksheet_name, worksheet_def, check_condition=False, conditions=[], nesting_level=0):
        # the worksheet might exist
        worksheet = self.worksheet_by_name(worksheet_name=worksheet_name, suppress_log=True, nesting_level=nesting_level+1)
        if worksheet:
            warn(f"worksheet [{worksheet_name}] exists, will not be creates", nesting_level=nesting_level)
            return []


        # create the worksheet with right dimensions and in the right place with right freezing
        worksheet_add_request = build_add_worksheet_request(worksheet_name=worksheet_name, sheet_index=worksheet_def.get('index', None), num_rows=worksheet_def['num-rows'], num_cols=worksheet_def['num-columns'], frozen_rows=worksheet_def['frozen-rows'], frozen_cols=worksheet_def['frozen-columns'])

        return [worksheet_add_request]



    ''' format worksheets according to the specs in worksheet_defs
    '''
    def format_worksheets(self, worksheet_names, worksheet_defs, check_condition=False, conditions=[], nesting_level=0):
        values, requests = [], []
        for worksheet_name in worksheet_names:
            if worksheet_name in worksheet_defs:
                info(f"formatting worksheet {worksheet_name}", nesting_level=nesting_level)

                worksheet_format_values, worksheet_format_requests = self.format_worksheet(worksheet_name=worksheet_name, worksheet_def=worksheet_defs[worksheet_name])

            else:
                warn(f"worksheet {worksheet_name} : structure not defined", nesting_level=nesting_level)
                if '*' in worksheet_defs:
                    worksheet_def = worksheet_defs['*']
                    info(f"But a common structure (*) was defined for formatting [{worksheet_name}]", nesting_level=nesting_level)
                    worksheet_format_values, worksheet_format_requests = self.format_worksheet(worksheet_name=worksheet_name, worksheet_def=worksheet_defs[worksheet_name])
                else:
                    worksheet_format_values, worksheet_format_requests = [], []

            values = values + worksheet_format_values
            requests = requests + worksheet_format_requests

    
        # finally update in batch
        self.update_in_batch(values=values, requests=requests, requester='format_worksheets', nesting_level=nesting_level+1)



    ''' format a worksheet according to spec defined in worksheet_def
    '''
    def format_worksheet(self, worksheet_name, worksheet_def, check_condition=False, conditions=[], nesting_level=0):
        # get the worksheet
        worksheet = self.worksheet_by_name(worksheet_name=worksheet_name, nesting_level=nesting_level+1)
        if not worksheet:
            return []

        values, requests = [], []

        # clear conditional formats
        conditional_formats = self.get_conditional_formats()
        number_of_rules = len(conditional_formats.get(worksheet_name, []))
        clear_conditional_formats_requests = worksheet.clear_conditional_formats_requests(number_of_rules=number_of_rules)
        requests = requests + clear_conditional_formats_requests


        # format worksheet requests
        worksheets_dict = self.worksheets_as_dict()
        format_worksheet_vals, format_worksheet_requests = worksheet.format_worksheet_requests(worksheet_def=worksheet_def, worksheets_dict=worksheets_dict)
        values = values + format_worksheet_vals
        requests = requests + format_worksheet_requests

        return values, requests
