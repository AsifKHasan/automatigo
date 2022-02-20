#!/usr/bin/env python3

import os.path
from os import path

import pygsheets
import urllib.request
import httplib2

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from PIL import Image

def authorize(cred_json_file):
    auth_context = {}

    _G = pygsheets.authorize(service_account_file=cred_json_file)

    credentials = ServiceAccountCredentials.from_json_keyfile_name(cred_json_file, scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'])
    credentials.authorize(httplib2.Http())

    gauth = GoogleAuth()
    gauth.credentials = credentials

    auth_context['_G'] = _G
    auth_context['service'] = discovery.build('sheets', 'v4', credentials=credentials)
    auth_context['drive'] = GoogleDrive(gauth)

    return auth_context

def hex_to_rgba(color_hex):
    color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4, 6))
    return {'red': color[0]/255, 'green': color[1]/255, 'blue': color[2]/255, 'alpha': color[3]/255}

def insert_dimension_request(ws, dimension, at_index, count, inherit_from_before):
    return {
        'insertDimension': {
            'range': dimension_range_object(ws, dimension, at_index, at_index + count), 'inheritFromBefore': inherit_from_before
        }
    }

def insert_rows_before(sheet, ws, at_index, count):
    sheet.custom_request(insert_dimension_request(ws, 'ROWS', at_index, count, True), None)

def insert_rows_after(sheet, ws, at_index, count):
    sheet.custom_request(insert_dimension_request(ws, 'ROWS', at_index, count, False), None)

def range_object(ws, start_row, end_row, start_col, end_col):
    return {'sheetId': ws.id, 'startRowIndex': start_row, 'endRowIndex': end_row, 'startColumnIndex': start_col, 'endColumnIndex': end_col}

def dimension_range_object(ws, dimension, startIndex, endIndex):
    return {'sheetId': ws.id, 'dimension': dimension, 'startIndex': startIndex, 'endIndex': endIndex}

def delete_dimension_request(ws, dimension, startIndex, endIndex):
    return {
        'deleteDimension': {
            'range': dimension_range_object(ws, dimension, startIndex, endIndex)
        }
    }

def delete_dimension(sheet, ws, dimension, startIndex, endIndex):
    sheet.custom_request(delete_dimension_request(sheet, ws, dimension, startIndex, endIndex), None)

def resize_dimension_request(ws, dimension, start_index, size):
    fields = []
    fields.append('pixelSize')
    return {
        'updateDimensionProperties' : {
            'range' : dimension_range_object(ws, dimension, start_index, start_index + 1),
            'properties': {'pixelSize': size},
            'fields': ','.join(fields)
        }
    }

def resize_column(sheet, ws, column_index, width):
    sheet.custom_request(resize_dimension_request(sheet, ws, 'COLUMNS', column_index, width), None)

def freeze_request(ws, rows, cols):
    return {'updateSheetProperties': {'properties': {'sheetId': ws.id, 'gridProperties': {'frozenRowCount': rows, 'frozenColumnCount': cols}}, 'fields': 'gridProperties.frozenRowCount,gridProperties.frozenColumnCount'}}

def freeze(sheet, ws, rows, cols):
    sheet.custom_request(freeze_request(ws, rows, cols), None)

def format_range_request(ws, start_row, end_row, start_col, end_col, user_entered_value=None, font_family=None, font_size=None, bold=None, fg_color=None, bg_color=None, wrap_strategy=None, valign=None, halign=None, number_format=None, borders=None):
    fields = []
    user_entered_value_object = None
    if user_entered_value:
        if isinstance(user_entered_value, str):
            fields.append('userEnteredValue.stringValue')
            user_entered_value_object = {'stringValue': user_entered_value}
        elif isinstance(user_entered_value, (int, float)):
            fields.append('userEnteredValue.numberValue')
            user_entered_value_object = {'numberValue': user_entered_value}
        elif isinstance(user_entered_value, bool):
            fields.append('userEnteredValue.boolValue')
            user_entered_value_object = {'boolValue': user_entered_value}
        else:
            fields.append('userEnteredValue.stringValue')
            user_entered_value_object = {'stringValue': user_entered_value}

    if font_family: fields.append('userEnteredFormat.textFormat.fontFamily')
    if font_size: fields.append('userEnteredFormat.textFormat.fontSize')
    if bold: fields.append('userEnteredFormat.textFormat.bold')
    if fg_color: fields.append('userEnteredFormat.textFormat.foregroundColor')

    if bg_color: fields.append('userEnteredFormat.backgroundColor')
    if valign: fields.append('userEnteredFormat.verticalAlignment')
    if halign: fields.append('userEnteredFormat.horizontalAlignment')
    if wrap_strategy: fields.append('userEnteredFormat.wrapStrategy')
    if number_format: fields.append('userEnteredFormat.numberFormat')
    if borders: fields.append('userEnteredFormat.borders')

    return {
      'repeatCell': {
        'range': range_object(ws, start_row, end_row, start_col, end_col),
        'cell': {
          'userEnteredValue': user_entered_value_object,
          'userEnteredFormat': {
            'verticalAlignment': valign,
            'horizontalAlignment': halign,
            'wrapStrategy': wrap_strategy,
            'numberFormat': number_format,
            'backgroundColor': None if bg_color is None else hex_to_rgba(bg_color),
            'borders': borders,
            'textFormat': {
              'foregroundColor': None if fg_color is None else hex_to_rgba(fg_color),
              'fontFamily': font_family,
              'fontSize': font_size,
              'bold': bold
            }
          }
        },
        'fields': ','.join(fields)
      }
    }

def format_range(sheet, ws, start_row, end_row, start_col, end_col, user_entered_value=None, font_family=None, font_size=None, bold=None, fg_color=None, bg_color=None, wrap_strategy=None, valign=None, halign=None, number_format=None, borders=None):
    sheet.custom_request(format_range_request(ws, start_row, end_row, start_col, end_col, user_entered_value, font_family, font_size, bold, fg_color, bg_color, wrap_strategy, valign, halign, number_format, borders), None)

def border_range_request(ws, start_row, end_row, start_col, end_col, borders=None):
    return {
      'updateBorders': {
        'range': range_object(ws, start_row, end_row, start_col, end_col),
        'top': borders['top'],
        'right': borders['right'],
        'bottom': borders['bottom'],
        'left': borders['left']
      }
    }

def border_range(sheet, ws, start_row, end_row, start_col, end_col, borders=None):
    sheet.custom_request(border_range_request(ws, start_row, end_row, start_col, end_col, borders), None)

def merge_cells_request(ws, start_row, end_row, start_col, end_col):
    return {
      'mergeCells': {
        'range': range_object(ws, start_row, end_row, start_col, end_col),
        'mergeType': 'MERGE_ALL'
      }
    }

def merge_cells(sheet, ws, start_row, end_row, start_col, end_col):
    sheet.custom_request(merge_cells_request(ws, start_row, end_row, start_col, end_col), None)

def init_worksheet_request(ws, num_rows=100, num_cols=4, frozen_rows=2, frozen_cols=0, col_def=None):
    requests = []

    # freeze first row
    requests.append(freeze_request(ws, frozen_rows, frozen_cols))

    # valign, font etc. for full worksheet
    requests.append(format_range_request(ws, 0, num_rows, 0, num_cols, font_family='Calibri', font_size=10, bold=False, fg_color='00000000', wrap_strategy='WRAP', valign='MIDDLE'))

    # column size, alignment, format
    for col_letter, col_data in col_def.items():
        requests.append(resize_dimension_request(ws, 'COLUMNS', col_data['col-num'], col_data['width']))
        requests.append(format_range_request(ws, 0, num_rows, col_data['col-num'], col_data['col-num'] + 1, None, None, bold=None, fg_color=None, bg_color=None, wrap_strategy=None, valign=None, halign=col_data['halign'], number_format=col_data['number-format']))

        # header cells - row 1
        requests.append(format_range_request(ws, 1, 2, col_data['col-num'], col_data['col-num'] + 1, user_entered_value=col_data['header-text'], bold=True, bg_color=col_data['header-bg-color']))

    return requests

def init_worksheet(sheet, ws_title, num_rows=100, num_cols=4, frozen_rows=2, frozen_cols=0, col_def=None, index=None):

    # if worksheet exists, delete it and create again
    try:
        ws = sheet.worksheet_by_title(ws_title)
        sheet.del_worksheet(ws)
    except pygsheets.exceptions.WorksheetNotFound:
        pass

    ws = sheet.add_worksheet(ws_title, rows=num_rows, cols=num_cols, index=index)

    sheet.custom_request(init_worksheet_request(ws, num_rows, num_cols, frozen_rows, frozen_cols, col_def), None)

    return ws

def download_image(image_formula, tmp_dir, row_height):
    '''
        image_formula liiks like
        "http://documents.biasl.net/data/projects/rhd/filling-station-367x221.png", 3'\
        or this
        "http://documents.biasl.net/data/res/logo/rhd-logo-200x200.png", 4, 150, 150
    '''
    s = image_formula.replace('"', '').split(',')
    url, local_path, mode = None, None, None

    # the first item is url
    if len(s) >= 1:
        url = s[0]
        # download image in url into localpath
        try:
            local_path = '{0}/{1}'.format(tmp_dir, url.split('/')[-1])
            # if the image is already in the local_path, we do not download it
            if path.exists(local_path):
                pass
            else:
                urllib.request.urlretrieve(url, local_path)
        except:
            print('.... could not download file: {0}'.format(url))
            return None

    # get the image dimensions
    try:
        im = Image.open(local_path)
        im_width, im_height = im.size
        if 'dpi' in im.info:
            im_dpi = im.info['dpi']
        else:
            im_dpi = (96, 96)

        aspect_ratio = (im_width / im_height)
    except:
        print('.... could not get dimesnion for image: {0}'.format(local_path))
        return None

    # the second item is mode - can be 1, 3 or 4
    if len(s) >= 2:
        mode = int(s[1])
    else:
        print('.... image link mode not found in formula: {0}'.format(image_formula))
        return None

    # image link is based on row height
    if mode == 1:
        height = row_height
        width = int(height * aspect_ratio)
        print('.... adjusting image {0} at {1}x{2}-{3} based on row height {4}'.format(local_path, width, height, im_dpi, row_height))
        return {'url': url, 'path': local_path, 'height': height, 'width': width, 'dpi': im_dpi}

    # image link is without height, width - use actual image size
    if mode == 3:
        print('.... keeping image {0} at {1}x{2}-{3} as-is'.format(local_path, im_width, im_height, im_dpi))
        return {'url': url, 'path': local_path, 'height': im_height, 'width': im_width, 'dpi': im_dpi}

    # image link specifies height and width, use those
    if mode == 4 and len(s) == 4:
        print('.... image {0} at {1}x{2}-{3} size specified'.format(local_path, im_width, im_height, im_dpi))
        return {'url': url, 'path': local_path, 'height': int(s[2]), 'width': int(s[3]), 'dpi': im_dpi}
    else:
        print('.... image link does not specify height and width: {0}'.format(image_formula))
        return None
