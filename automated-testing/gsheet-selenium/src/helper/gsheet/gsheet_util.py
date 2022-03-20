#!/usr/bin/env python
'''
'''

import os.path
from os import path

import pygsheets
import urllib.request
from PIL import Image

COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def hex_to_rgba(color_hex):
    color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4, 6))
    return {'red': color[0]/255, 'green': color[1]/255, 'blue': color[2]/255, 'alpha': color[3]/255}

def range_object(ws, start_row, end_row, start_col, end_col):
    return {'sheetId': ws.id, 'startRowIndex': start_row, 'endRowIndex': end_row, 'startColumnIndex': start_col, 'endColumnIndex': end_col}

def dimension_range_object(ws, dimension, startIndex, endIndex):
    return {'sheetId': ws.id, 'dimension': dimension, 'startIndex': startIndex, 'endIndex': endIndex}

def delete_dimension_request(sheet, ws, dimension, startIndex, endIndex):
    return {
        'deleteDimension': {
            'range': dimension_range_object(ws, dimension, startIndex, endIndex)
        }
    }

def delete_dimension(sheet, ws, dimension, startIndex, endIndex):
    sheet.custom_request(delete_dimension_request(sheet, ws, dimension, startIndex, endIndex), None)

def resize_dimension_request(sheet, ws, dimension, start_index, size):
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

def freeze_request(sheet, ws, rows, cols):
    return {'updateSheetProperties': {'properties': {'sheetId': ws.id, 'gridProperties': {'frozenRowCount': rows, 'frozenColumnCount': cols}}, 'fields': 'gridProperties.frozenRowCount,gridProperties.frozenColumnCount'}}

def freeze(sheet, ws, rows, cols):
    sheet.custom_request(freeze_request(sheet, ws, rows, cols), None)

def format_range_request(sheet, ws, start_row, end_row, start_col, end_col, user_entered_value=None, font_family=None, font_size=None, bold=None, fg_color=None, bg_color=None, wrap_strategy=None, valign=None, halign=None, number_format=None, borders=None):
    fields = []
    if user_entered_value: fields.append('userEnteredValue.stringValue')

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
          'userEnteredValue': {
            'stringValue': user_entered_value
            },
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
    sheet.custom_request(format_range_request(sheet, ws, start_row, end_row, start_col, end_col, user_entered_value, font_family, font_size, bold, fg_color, bg_color, wrap_strategy, valign, halign, number_format, borders), None)

def border_range_request(sheet, ws, start_row, end_row, start_col, end_col, borders=None):
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
    sheet.custom_request(border_range_request(sheet, ws, start_row, end_row, start_col, end_col, borders), None)

def merge_cells_request(sheet, ws, start_row, end_row, start_col, end_col):
    return {
      'mergeCells': {
        'range': range_object(ws, start_row, end_row, start_col, end_col),
        'mergeType': 'MERGE_ALL'
      }
    }

def merge_cells(sheet, ws, start_row, end_row, start_col, end_col):
    sheet.custom_request(merge_cells_request(sheet, ws, start_row, end_row, start_col, end_col), None)

def init_worksheet(sheet, ws_title, num_rows=100, num_cols=4, frozen_rows=2, frozen_cols=0, col_def=None):
    # if worksheet exists, delete it and create again
    try:
        ws = sheet.worksheet_by_title(ws_title)
        sheet.del_worksheet(ws)
    except pygsheets.exceptions.WorksheetNotFound:
        pass

    ws = sheet.add_worksheet(ws_title, rows=num_rows, cols=num_cols)

    # freeze first row
    freeze(sheet, ws, frozen_rows, frozen_cols)

    # valign, font etc. for full worksheet
    format_range(sheet, ws, 0, num_rows, 0, num_cols, 'Calibri', 10, bold=False, fg_color='00000000', bg_color=None, wrap_strategy='WRAP', valign='MIDDLE', halign=None, number_format=None)

    # column size, alignment, format
    for col_letter, col_data in col_def.items():
        ws.adjust_column_width(start=col_data['idx'], end=None, pixel_size=col_data['size'])
        format_range(sheet, ws, 0, num_rows, col_data['idx'], col_data['idx'] + 1, None, None, bold=None, fg_color=None, bg_color=None, wrap_strategy=None, valign=None, halign=col_data['halign'], number_format=col_data['numberFormat'])

    return ws
