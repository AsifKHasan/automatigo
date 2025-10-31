#!/usr/bin/env python

# Resume structure
WORKSHEET_STRUCTURE_RESUME = {
    "00-layout": {
        "num-rows": 27,
        "num-columns": 5,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "valign": "top", "wrap": True},
            "B": {"size": 30, "halign": "left", "valign": "top", "wrap": True},
            "C": {"size": 250, "halign": "left", "valign": "top", "wrap": True},
            "D": {"size": 250, "halign": "left", "valign": "top", "wrap": True},
            "E": {"size": 270, "halign": "center", "valign": "top", "wrap": True},
        },
        "rows": {
            "1": {
                "size": 21,
            },
            "2": {
                "size": 21,
            },
            "3": {
                "size": 21,
            },
            "4": {
                "size": 21,
            },
            "5": {
                "size": 21,
            },
            "6": {
                "size": 8,
            },
            "7": {
                "size": 21,
            },
            "8": {
                "size": 21,
            },
            "9": {
                "size": 8,
            },
            "10": {
                "size": 21,
            },
            "11": {
                "size": 21,
            },
            "12": {
                "size": 8,
            },
            "13": {
                "size": 21,
            },
            "14": {
                "size": 21,
            },
            "15": {
                "size": 8,
            },
            "16": {
                "size": 21,
            },
            "17": {
                "size": 21,
            },
            "18": {
                "size": 8,
            },
            "19": {
                "size": 21,
            },
            "20": {
                "size": 21,
            },
            "21": {
                "size": 8,
            },
            "22": {
                "size": 21,
            },
            "23": {
                "size": 21,
            },
            "24": {
                "size": 8,
            },
            "25": {
                "size": 21,
            },
            "26": {
                "size": 21,
            },
            "27": {
                "size": 8,
            },
            "28": {
                "size": 21,
            },
            "29": {
                "size": 21,
            },
        },
        "review-notes": True,
        "ranges": {
            # whole worksheet
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            # -toc-new link
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            # column size in pixels
            "B1:E1": {
                "halign": "center",
            },
            # column label - review-notes
            "A2": {
                "value": "review-notes",
                "halign": "left",
                "weight": "bold",
            },
            # column label - content
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "weight": "bold",
                "merge": True,
            },
            # name of resource
            "B3": {
                "value": "1",
                "weight": "bold",
            },
            "C3": {
                "value": "NAME OF RESOURCE",
                "weight": "bold",
            },
            "D3": {
                "value": "='01-personal'!D3",
            },
            # date of birth
            "B4": {
                "value": "2",
                "weight": "bold",
            },
            "C4": {
                "value": "DATE OF BIRTH",
                "weight": "bold",
            },
            "D4": {
                "value": "='01-personal'!D5",
            },
            # nationality
            "B5": {
                "value": "3",
                "weight": "bold",
            },
            "C5": {
                "value": "NATIONALITY",
                "weight": "bold",
            },
            "D5": {
                "value": "='01-personal'!D6",
            },
            # nationality
            "E3:E5": {
                "value": "='01-personal'!E3",
                "merge": True 
            },

            # summary of prefessional experience
            "B6": {
                "value": "",
            },
            "B7": {
                "value": "4",
                "weight": "bold",
            },
            "C7:E7": {
                "value": "SUMMARY OF PROFESSIONAL EXPERIENCE",
                "weight": "bold",
                "merge": True,
            },
            "B8": {
                "value": "02-career-highlight",
                "ws-name-to-link": "02-career-highlight",
                "note": '{"content": "free"}',
            },
            # education
            "B9": {
                "value": "",
            },
            "B10": {
                "value": "5",
                "weight": "bold",
            },
            "C10:E10": {
                "value": "EDUCATION",
                "weight": "bold",
                "merge": True,
            },
            "B11": {
                "value": "03-education",
                "ws-name-to-link": "03-education",
                "note": '{"content": "free"}',
            },
            # employment record
            "B12": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B13": {
                "value": "6a",
                "weight": "bold",
            },
            "C13:E13": {
                "value": "EMPLOYMENT RECORD",
                "weight": "bold",
                "merge": True,
            },
            "B14": {
                "value": "06-job-history",
                "ws-name-to-link": "06-job-history",
                "note": '{"content": "free"}',
            },
            # professional experience
            "B15": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B16": {
                "value": "6b",
                "weight": "bold",
            },
            "C16:E16": {
                "value": "PROFESSIONAL EXPERIENCE",
                "weight": "bold",
                "merge": True,
            },
            "B17": {
                "value": "07-project-roles",
                "ws-name-to-link": "07-project-roles",
                "note": '{"content": "free"}',
            },
            # technical expertise
            "B18": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B19": {
                "value": "7",
                "weight": "bold",
            },
            "C19:E19": {
                "value": "TECHNICAL EXPERTISE",
                "weight": "bold",
                "merge": True,
            },
            "B20": {
                "value": "05-technical-expertise",
                "ws-name-to-link": "05-technical-expertise",
                "note": '{"content": "free"}',
            },
            # professional training
            "B21": {
                "value": "",
            },
            "B22": {
                "value": "8a",
                "weight": "bold",
            },
            "C22:E22": {
                "value": "PROFESSIONAL TRAINING",
                "weight": "bold",
                "merge": True,
            },
            "B23": {
                "value": "08-training",
                "ws-name-to-link": "08-training",
                "note": '{"content": "free"}',
            },
            # professional certificates
            "B24": {
                "value": "",
            },
            "B25": {
                "value": "8b",
                "weight": "bold",
            },
            "C25:E25": {
                "value": "PROFESSIONAL CERTIFICATIONS",
                "weight": "bold",
                "merge": True,
            },
            "B26": {
                "value": "09-certification",
                "ws-name-to-link": "09-certification",
                "note": '{"content": "free"}',
            },
            # language proficency
            "B27": {
                "value": "",
            },
            "B28": {
                "value": "9",
                "weight": "bold",
            },
            "C28:E28": {
                "value": "LANGUAGES & DEGREE OF PROFICIENCY",
                "weight": "bold",
                "merge": True,
            },
            "B29": {
                "value": "11-language-proficiency",
                "ws-name-to-link": "11-language-proficiency",
                "note": '{"content": "free"}',
            },
        },
        "cell-empty-markers": [
            "B3:E5",
        ],
    },
    "00-layout-USAID": {
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 60},
            "C": {"size": 340},
            "D": {"size": 400},
        },
        "rows": {
            "5": {"size": 10},
            "8": {"size": 10},
            "11": {"size": 10},
            "14": {"size": 10},
            "17": {"size": 10},
        },
        "ranges": {
            "A1": {"value": "-toc-new", "ws-name-to-link": "-toc-new"},
            "A2": {"value": "review-notes", "weight": "bold"},
            "B2:D2": {"value": "content", "weight": "bold", "merge": True},
            "B3:C3": {
                "value": "Name:",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "merge": True,
            },
            "D3": {
                "value": "Proposed Position:",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4": {"weight": "normal", "fgcolor": "#434343", "border-color": "#B7B7B7"},
            "C4": {
                "value": "='01-personal'!D3",
                "weight": "normal",
                "fgcolor": "#434343",
                "border-color": "#B7B7B7",
                "merge": True,
            },
            "D4": {"weight": "normal", "fgcolor": "#434343", "border-color": "#B7B7B7"},
            "B5:D5": {"merge": True, "font-size": 4},
            "B6:D6": {
                "value": "Summary of personnel experience",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#FFFFFF",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B7:D7": {
                "value": "02-career-highlight",
                "ws-name-to-link": "02-career-highlight",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B8:D8": {"merge": True, "font-size": 4},
            "B9:D9": {
                "value": "EDUCATION:",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#FFFFFF",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B10:D10": {
                "value": "03-education",
                "ws-name-to-link": "03-education",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B11:D11": {"merge": True, "font-size": 4},
            "B12:D12": {
                "value": "PROFESSIONAL EXPERIENCE:",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#FFFFFF",
                "merge": True,
                "note": '{"content": "free", "new-page": true}',
            },
            "B13:D13": {
                "value": "06-job-history-USAID-FFBT",
                "ws-name-to-link": "06-job-history-USAID-FFBT",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B14:D14": {"merge": True, "font-size": 4},
            "B15:D15": {
                "value": "LANGUAGE:",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#FFFFFF",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B16:D16": {
                "value": "11-language-proficiency",
                "ws-name-to-link": "11-language-proficiency",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B17:D17": {"merge": True, "font-size": 4},
            "B18:D18": {
                "value": "REFERENCES:",
                "weight": "bold",
                "fgcolor": "#666666",
                "bgcolor": "#FFFFFF",
                "merge": True,
                "note": '{"content": "free"}',
            },
            "B19:D19": {
                "value": "16-references",
                "ws-name-to-link": "16-references",
                "merge": True,
                "note": '{"content": "free"}',
            },
        },
        "cell-empty-markers": [
            "B4:D4",
        ],
    },
    "00-layout-MRA-OMS": {
        "num-rows": 49,
        "num-columns": 9,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {
                "size": 100,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "B": {
                "size": 40,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "C": {
                "size": 180,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "D": {
                "size": 50,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "E": {
                "size": 30,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "F": {
                "size": 50,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "G": {
                "size": 30,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "H": {
                "size": 300,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "I": {
                "size": 320,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:I1": {
                "halign": "center",
            },
            "B2:I2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3:G3": {
                "merge": True,
                "halign": "left",
                "value": "Name of the Consultant",
            },
            "H3:I3": {
                "merge": True,
                "halign": "left",
                "value": "DOER Services Ltd.",
            },
            "B4:G4": {
                "merge": True,
                "halign": "left",
                "weight": "bold",
                "value": "RFP IDENTIFICATION NO:",
            },
            "H4:I4": {
                "merge": True,
                "halign": "left",
                "weight": "bold",
                "value": "53.04.0000.002.07.011.23-1306",
            },
            "B5:G5": {
                "merge": True,
                "halign": "left",
                "value": "Name of the Client",
            },
            "H5:I5": {
                "merge": True,
                "halign": "left",
                "value": "Microcredit Regulatory Authority",
            },
            "B7": {
                "value": "1",
            },
            "C7:G7": {
                "value": "PROPOSED POSITION",
            },
            "H7": {
                "value": "",
            },
            "B8": {
                "value": "2",
            },
            "C8": {
                "value": "NAME OF RESOURCE",
            },
            "D8": {
                "value": "='01-personal'!D3",
            },
            "B9": {
                "value": "3",
            },
            "C9": {
                "value": "DATE OF BIRTH",
            },
            "D9": {
                "value": "='01-personal'!D5",
            },
            "B10": {
                "value": "4",
            },
            "C10": {
                "value": "NATIONALITY",
            },
            "D10": {
                "value": "='01-personal'!D6",
            },
            # 'B3:E6': {'border-color': '#B7B7B7', },
            "B7": {
                "value": "",
            },
            "B8": {
                "value": "4",
            },
            "C8:E8": {
                "value": "SUMMARY OF PROFESSIONAL EXPERIENCE",
                "merge": True,
            },
            "B9": {
                "value": "02-career-highlight",
                "ws-name-to-link": "02-career-highlight",
                "note": '{"content": "free"}',
            },
            "B10": {
                "value": "",
            },
            "B11": {
                "value": "5",
            },
            "C11:E11": {
                "value": "EDUCATION",
                "merge": True,
            },
            "B12": {
                "value": "03-education",
                "ws-name-to-link": "03-education",
                "note": '{"content": "free"}',
            },
            "B13": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B14": {
                "value": "6",
            },
            "C14:E14": {
                "value": "EMPLOYMENT RECORD",
                "merge": True,
            },
            "B15": {
                "value": "06-job-history",
                "ws-name-to-link": "06-job-history",
                "note": '{"content": "free"}',
            },
            "B16": {
                "value": "",
            },
            "B17": {
                "value": "07-project-roles",
                "ws-name-to-link": "07-project-roles",
                "note": '{"content": "free"}',
            },
            "B18": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B19": {
                "value": "7",
            },
            "C19:E19": {
                "value": "TECHNICAL EXPERTISE",
                "merge": True,
            },
            "B20": {
                "value": "05-technical-expertise",
                "ws-name-to-link": "05-technical-expertise",
                "note": '{"content": "free"}',
            },
            "B21": {
                "value": "",
            },
            "B22": {
                "value": "8",
            },
            "C22:E22": {
                "value": "TRAINING AND CERTIFICATIONS",
                "merge": True,
            },
            "B23": {
                "value": "08-training",
                "ws-name-to-link": "08-training",
                "note": '{"content": "free"}',
            },
            "B24": {
                "value": "",
            },
            "B25": {
                "value": "09-certification",
                "ws-name-to-link": "09-certification",
                "note": '{"content": "free"}',
            },
            "B26": {
                "value": "",
            },
            "B27": {
                "value": "9",
            },
            "C27:E27": {
                "value": "LANGUAGES & DEGREE OF PROFICIENCY",
                "merge": True,
            },
            "B28": {
                "value": "11-language-proficiency",
                "ws-name-to-link": "11-language-proficiency",
                "note": '{"content": "free"}',
            },
        },
        "cell-empty-markers": [
            "B3:I5",
            "B7:I10",
            "B12:I13",
            "B15:I16",
            "B18:I19",
            "B21:I21",
            "B23:I24",
            "B26:I26",
            "B28:I29",
            "B31:I32",
            "B34:I35",
            "B37:I37",
            "B39:I39",
            "B41:I41",
            "D43",
            "F43",
            "D45:G47",
            "H45:I47",
            "D48:G49",
            "H48:I49",
        ],
    },
    "00-layout-RHD-TMC": {
        "num-rows": 28,
        "num-columns": 5,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "valign": "top", "wrap": True},
            "B": {"size": 30, "halign": "left", "valign": "top", "wrap": True},
            "C": {"size": 250, "halign": "left", "valign": "top", "wrap": True},
            "D": {"size": 250, "halign": "left", "valign": "top", "wrap": True},
            "E": {"size": 270, "halign": "center", "valign": "top", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "1",
            },
            "C3": {
                "value": "PROPOSED POSITION",
            },
            "D3": {
                "value": "",
            },
            "B4": {
                "value": "2",
            },
            "C4": {
                "value": "NAME OF RESOURCE",
            },
            "D4": {
                "value": "='01-personal'!D3",
            },
            "B5": {
                "value": "3",
            },
            "C5": {
                "value": "DATE OF BIRTH",
            },
            "D5": {
                "value": "='01-personal'!D5",
            },
            "B6": {
                "value": "4",
            },
            "C6": {
                "value": "NATIONALITY",
            },
            "D6": {
                "value": "='01-personal'!D6",
            },
            # 'B3:E6': {'border-color': '#B7B7B7', },
            "B7": {
                "value": "",
            },
            "B8": {
                "value": "4",
            },
            "C8:E8": {
                "value": "SUMMARY OF PROFESSIONAL EXPERIENCE",
                "merge": True,
            },
            "B9": {
                "value": "02-career-highlight",
                "ws-name-to-link": "02-career-highlight",
                "note": '{"content": "free"}',
            },
            "B10": {
                "value": "",
            },
            "B11": {
                "value": "5",
            },
            "C11:E11": {
                "value": "EDUCATION",
                "merge": True,
            },
            "B12": {
                "value": "03-education",
                "ws-name-to-link": "03-education",
                "note": '{"content": "free"}',
            },
            "B13": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B14": {
                "value": "6",
            },
            "C14:E14": {
                "value": "EMPLOYMENT RECORD",
                "merge": True,
            },
            "B15": {
                "value": "06-job-history",
                "ws-name-to-link": "06-job-history",
                "note": '{"content": "free"}',
            },
            "B16": {
                "value": "",
            },
            "B17": {
                "value": "07-project-roles",
                "ws-name-to-link": "07-project-roles",
                "note": '{"content": "free"}',
            },
            "B18": {
                "value": "",
                "note": '{"content": "free", "new-page": true}',
            },
            "B19": {
                "value": "7",
            },
            "C19:E19": {
                "value": "TECHNICAL EXPERTISE",
                "merge": True,
            },
            "B20": {
                "value": "05-technical-expertise",
                "ws-name-to-link": "05-technical-expertise",
                "note": '{"content": "free"}',
            },
            "B21": {
                "value": "",
            },
            "B22": {
                "value": "8",
            },
            "C22:E22": {
                "value": "TRAINING AND CERTIFICATIONS",
                "merge": True,
            },
            "B23": {
                "value": "08-training",
                "ws-name-to-link": "08-training",
                "note": '{"content": "free"}',
            },
            "B24": {
                "value": "",
            },
            "B25": {
                "value": "09-certification",
                "ws-name-to-link": "09-certification",
                "note": '{"content": "free"}',
            },
            "B26": {
                "value": "",
            },
            "B27": {
                "value": "9",
            },
            "C27:E27": {
                "value": "LANGUAGES & DEGREE OF PROFICIENCY",
                "merge": True,
            },
            "B28": {
                "value": "11-language-proficiency",
                "ws-name-to-link": "11-language-proficiency",
                "note": '{"content": "free"}',
            },
        },
        "cell-empty-markers": [
            "B3:E6",
        ],
    },
    "01-personal": {
        "num-columns": 5,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 30, "halign": "center", "wrap": True},
            "C": {"size": 130, "halign": "left", "wrap": True},
            "D": {"size": 320, "halign": "left", "wrap": True},
            "E": {"size": 320, "halign": "center", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": ["B3:Z"],
    },
    "02-career-highlight": {
        "num-columns": 4,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 150, "halign": "left", "wrap": True},
            "C": {"size": 30, "halign": "center", "wrap": True},
            "D": {"size": 620, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:D1": {
                "halign": "center",
            },
            "B2:D2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "03-education": {
        "num-columns": 5,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 80, "halign": "center", "wrap": True},
            "C": {"size": 210, "halign": "left", "wrap": True},
            "D": {"size": 210, "halign": "left", "wrap": True},
            "E": {"size": 300, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Year",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "Degree",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3": {
                "value": "Subject/Discipline",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "E3": {
                "value": "Institute",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "04-managerial-expertise": {
        "num-columns": 4,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 170, "halign": "left", "wrap": True},
            "C": {"size": 30, "halign": "center", "wrap": True},
            "D": {"size": 600, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:D1": {
                "halign": "center",
            },
            "B2:D2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Area",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3:D3": {
                "value": "Expertise",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "05-technical-expertise": {
        "num-columns": 4,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 170, "halign": "left", "wrap": True},
            "C": {"size": 30, "halign": "center", "wrap": True},
            "D": {"size": 600, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:D1": {
                "halign": "center",
            },
            "B2:D2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Area",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3:D3": {
                "value": "Expertise",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "06-job-history": {
        "num-columns": 5,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 60, "halign": "center", "wrap": True},
            "C": {"size": 60, "halign": "center", "wrap": True},
            "D": {"size": 30, "wrap": True},
            "E": {"size": 650, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "From",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "To",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3:E3": {
                "value": "Employment History",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "06-job-history-USAID": {
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 65, "halign": "center", "wrap": True},
            "C": {"size": 65, "halign": "center", "wrap": True},
            "D": {"size": 30, "wrap": True},
            "E": {"size": 640, "wrap": True},
        },
        "ranges": {
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "B1": {"value": "65", "halign": "center"},
            "C1": {"value": "65", "halign": "center"},
            "D1": {"value": "30", "halign": "center"},
            "E1": {"value": "640", "halign": "center"},
            "B2:E2": {"value": "content", "halign": "left", "merge": True},
        },
    },
    "07-project-roles": {
        "num-columns": 5,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 60, "halign": "center", "wrap": True},
            "C": {"size": 60, "halign": "center", "wrap": True},
            "D": {"size": 30, "wrap": True},
            "E": {"size": 650, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "From",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "To",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3:E3": {
                "value": "Company/Project/Position/ Relevant Technical and Management Experience",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "08-training": {
        "num-columns": 4,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 80, "halign": "center", "wrap": True},
            "C": {"size": 450, "halign": "left", "wrap": True},
            "D": {"size": 370, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:D1": {
                "halign": "center",
            },
            "B2:D2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Year",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "Training",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3": {
                "value": "Institute",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "09-certification": {
        "num-columns": 5,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 70, "halign": "center", "wrap": True},
            "C": {"size": 150, "halign": "left", "wrap": True},
            "D": {"size": 280, "halign": "left", "wrap": True},
            "E": {"size": 300, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Year",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "Vendor/OEM/ Subject",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3": {
                "value": "Certification",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "E3": {
                "value": "Details",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "10-membership": {
        "num-columns": 6,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 250, "halign": "left", "wrap": True},
            "C": {"size": 150, "halign": "left", "wrap": True},
            "D": {"size": 125, "halign": "center", "wrap": True},
            "E": {"size": 125, "halign": "center", "wrap": True},
            "F": {"size": 150, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:F1": {
                "halign": "center",
            },
            "B2:F2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Professional Organization/Society",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "Membership Rank/Level",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3": {
                "value": "Membership ID/Number",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "E3": {
                "value": "Member Since",
                "halign": "center",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "F3": {
                "value": "Details",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "11-language-proficiency": {
        "num-columns": 5,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 110, "halign": "left", "wrap": True},
            "C": {"size": 230, "halign": "left", "wrap": True},
            "D": {"size": 230, "halign": "left", "wrap": True},
            "E": {"size": 230, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:E1": {
                "halign": "center",
            },
            "B2:E2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Language",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "Speaking",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3": {
                "value": "Reading",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "E3": {
                "value": "Writing",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "12-contact": {
        "num-columns": 3,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 200, "halign": "left", "wrap": True},
            "C": {"size": 600, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:C1": {
                "halign": "center",
            },
            "B2:C2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:C4",
        ],
    },
    "13-educational-certificates": {
        "num-columns": 2,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 800, "halign": "center", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1": {
                "halign": "center",
            },
            "B2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "14-vendor-certificates": {
        "num-columns": 2,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 800, "halign": "center", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1": {
                "halign": "center",
            },
            "B2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "15-institutional-certificates": {
        "num-columns": 2,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 800, "halign": "center", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1": {
                "halign": "center",
            },
            "B2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "16-references": {
        "num-columns": 6,
        "frozen-rows": 3,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 140, "halign": "left", "wrap": True},
            "C": {"size": 150, "halign": "left", "wrap": True},
            "D": {"size": 190, "halign": "left", "wrap": True},
            "E": {"size": 190, "halign": "left", "wrap": True},
            "F": {"size": 130, "halign": "left", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:F1": {
                "halign": "center",
            },
            "B2:F2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
            "B3": {
                "value": "Name",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
                "note": '{"repeat-rows": 1}',
            },
            "C3": {
                "value": "Position",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "D3": {
                "value": "Company",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "E3": {
                "value": "Email",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "F3": {
                "value": "Phone Number",
                "halign": "left",
                "bgcolor": "#F3F3F3",
                "border-color": "#B7B7B7",
            },
            "B4:Z": {
                "border-color": "#B7B7B7",
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "z-head": {
        "num-columns": 3,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 600, "halign": "left", "wrap": True},
            "C": {"size": 200, "halign": "right", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:C1": {
                "halign": "center",
            },
            "B2:C2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
    "z-foot": {
        "num-columns": 3,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 600, "halign": "left", "wrap": True},
            "C": {"size": 200, "halign": "right", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            "A1:Z": {
                "valign": "top",
                "wrap": True,
                "bgcolor": "#FFFFFF",
                "border-color": "#B7B7B7",
                "no-border": True,
            },
            "A1": {
                "value": "-toc-new",
                "ws-name-to-link": "-toc-new",
                "halign": "left",
            },
            "A2": {
                "value": "review-notes",
                "halign": "left",
            },
            "B1:C1": {
                "halign": "center",
            },
            "B2:C2": {
                "value": "content",
                "halign": "left",
                "merge": True,
            },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
    },
}

# Resume structure
WORKSHEET_STRUCTURE_PDS = {
    '00-layout': {
        'num-rows': 38,
        'num-columns': 4,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'size': 100, 'halign': 'left', 'wrap': True, },
            'B': {'size': 240, 'halign': 'left', 'wrap': True, },
            'C': {'size': 240, 'halign': 'left', 'wrap': True, },
            'D': {'size': 320, 'halign': 'left', 'wrap': True, },
        },
        'review-notes': True,
        'ranges': {
            # row 1
            # link to -toc-new
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', },
            # label - review-notes
            # column sizes in pixel
            'B1:D1': {'halign': 'center', },

            # row 2
            'A2': {'value': 'review-notes', 'weight': 'bold', },
            # label - content
            'B2:D2': {'value': 'content', 'weight': 'bold', 'merge': True, },

            # row 3
            # label - Assignment Name
            'B3:C3': {'value': 'Assignment Name:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Country
            'D3': {'value': 'Country:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 4
            # content - Assignment Name
            'B4:C4': {'value': "='01-summary'!C3", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },
            # content - Country
            'D4': {'value': "='01-summary'!C4", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },

            # row 5
            # label - Location within Country
            'B5:C5': {'value': 'Location within Country:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Duration of assignment (months)
            'D5': {'value': 'Duration of assignment (months):', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 6
            # content - Assignment Location within country
            'B6:C6': {'value': "='01-summary'!C7", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },
            # content - Duration of assignment (months)
            'D6': {'value': "='01-summary'!C8", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },

            # row 7
            # label - Name of Client
            'B7:C7': {'value': 'Name of Client:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Approximate value of the Project (In BDT)
            'D7': {'value': 'Approximate value of the Project (In BDT):', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 8
            # content - Name of Client
            'B8:C8': {'value': "='01-summary'!C9", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },
            # content - Total Revenue
            'D8': {'value': "='02-revenue'!C3", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },

            # row 9
            # label - Address
            'B9:C9': {'value': 'Address', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Approx. value of the services provided by your firm under the contract
            'D9': {'value': 'Approx. value of the services provided by your firm under the contract:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 10
            # content - Address
            'B10:C10': {'value': "='01-summary'!C10", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"keep-line-breaks": true}', },
            # content - Total Revenue
            'D10': {'value': "='02-revenue'!C3", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },

            # row 11
            # label - Start Date (Month/Year)
            'B11': {'value': 'Start Date (Month/Year):', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # label - Completion Date (Month/Year)
            'C11': {'value': 'Completion Date (Month/Year):', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # label - No. of person-months of the assignment
            'D11': {'value': 'No. of person-months of the assignment:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 12
            # content - Start Date
            'B12': {'value': "='01-summary'!C13", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },
            # content - Completion Date
            'C12': {'value': "='01-summary'!C13", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },
            # content - Professional Staff-Months
            'D12': {'value': "='01-summary'!C12", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },

            # row 13
            # label - Name of joint venture partner or sub-consultants, if any
            'B13:C13': {'value': 'Name of joint venture partner or sub-consultants, if any:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - No. of months of Professional Staff Provided by your firm under the contract
            'D13': {'value': 'No. of months of Professional Staff Provided by your firm under the contract:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 16
            # content - 04-joint-venture
            'B14:C14': {'value': '04-joint-venture', 'ws-name-to-link': '04-joint-venture', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, },
            # content - Professional Staff-Months
            'D14': {'value': "='01-summary'!C12", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', },

            # row 15
            'B15:D15': {'merge': True},

            # row 16
            # label - Name of Senior Staff (Project Director/Coordinator, Team Leader) Involved and Functions Performed
            'B16:D16': {'value': 'Name of Senior Staff (Project Director/Coordinator, Team Leader) Involved and Functions Performed:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 17
            # content - 05-people
            'B17:D17': {'value': '05-people', 'ws-name-to-link': '05-people', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 18
            'B18:D18': {'merge': True, },

            # row 19
            # label - Narrative Description of Project
            'B19:D19': {'value': 'Narrative Description of Project:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free", "new-page": true}', },

            # row 20
            # label - Project Description
            'B20:D20': {'value': 'Project Description', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },

            # row 21
            # content - 06-description
            'B21:D21': {'value': '06-description', 'ws-name-to-link': '06-description', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 22
            'B22:D22': {'merge': True, },

            # row 23
            # label - Functionality
            'B23:D23': {'value': 'Functionality', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },

            # row 24
            # content - 07-functionality
            'B24:D24': {'value': '07-functionality', 'ws-name-to-link': '07-functionality', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 25
            'B25:D25': {'merge': True, },

            # row 26
            # label - Technology
            'B26:D26': {'value': 'Technology', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },

            # row 27
            # content - 08-technology
            'B27:D27': {'value': '08-technology', 'ws-name-to-link': '08-technology', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 28
            'B28:D28': {'merge': True, },

            # row 29
            # label - Narrative Descriptions of works performed by your organization
            'B29:D29': {'value': 'Narrative Descriptions of works performed by your organization:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free", "new-page": true}', },

            # row 30
            # label - Services Provided
            'B30:D30': {'value': 'Services Provided', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },

            # row 31
            # content - 09-services
            'B31:D31': {'value': '09-services', 'ws-name-to-link': '09-services', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 32
            'B32:D32': {'merge': True, },

            # row 33
            # label - Processes Adopted
            'B33:D33': {'value': 'Processes Adopted', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },

            # row 34
            # content - 10-process
            'B34:D34': {'value': '10-process', 'ws-name-to-link': '10-process', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 35
            'B35:D35': {'merge': True, },

            # row 36
            # label - Firm’s Name
            'B36': {'value': "Firm's Name:", 'weight': 'normal', 'fgcolor': '#666666', 'bgcolor': '#FFFFFF', 'border-color': '#B7B7B7', },
            # content - 10-process
            'C36:D36': {'value': 'DOER Services Ltd.', 'weight': 'normal', 'fgcolor': '#666666', 'bgcolor': '#FFFFFF', 'border-color': '#B7B7B7', 'merge': True, },

            # row 37-38
            # label - Authorized Signature
            'B37:B38': {'value': 'Authorized Signature:', 'weight': 'normal', 'fgcolor': '#666666', 'bgcolor': '#FFFFFF', 'border-color': '#B7B7B7', 'merge': True, },

            # row 37-38
            # content - Authorized Signature
            'C37:D38': {'value': None, 'weight': 'normal', 'fgcolor': '#666666', 'bgcolor': '#FFFFFF', 'border-color': '#B7B7B7', 'merge': True, },
        },
        'cell-empty-markers': [
            'B3:D14',
            'B16:D17',
            'B19:D21',
            'B23:D24',
            'B26:D27',
            'B29:D31',
            'B33:D34',
            'C36:D36',
        ],
    },
    '00-layout-USAID': {
        'num-rows': 24,
        'num-columns': 8,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'size': 100, 'halign': 'left', 'wrap': True, },
            'B': {'size':  30, 'halign': 'left', 'wrap': True, },
            'C': {'size': 160, 'halign': 'left', 'wrap': True, },
            'D': {'size':  70, 'halign': 'left', 'wrap': True, },
            'E': {'size': 160, 'halign': 'left', 'wrap': True, },
            'F': {'size':  30, 'halign': 'left', 'wrap': True, },
            'G': {'size': 170, 'halign': 'left', 'wrap': True, },
            'H': {'size': 240, 'halign': 'left', 'wrap': True, },
        },
        'review-notes': True,
        'ranges': {
            # row 1
            # link to -toc-new
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', },
            # column sizes in pixel
            'B1:H1': {'halign': 'center', },

            # row 2
            # label - review-notes
            'A2': {'value': 'review-notes', 'weight': 'bold', },
            # label - content
            'B2:H2': {'value': 'content', 'weight': 'bold', 'merge': True, },

            # row 3
            # label - PAST PERFORMANCE REPORT - SHORT FORM						
            'B3:H3': {'value': 'PAST PERFORMANCE REPORT - SHORT FORM', 'weight': 'normal', 'fgcolor': '#FFFFFF', 'bgcolor': '#45818e', 'border-color': '#B7B7B7', 'halign': 'center', 'merge': True, },

            # row 3
            # label - 1.
            'B4:B5': {'value': '1.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Name of Contracting Entity
            'C4:E4': {'value': 'Name of Contracting Entity:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - 2.
            'F4': {'value': '2.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Contract No.
            'G4': {'value': 'Contract No.:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Contract No.
            'H4': {'value': "='01-summary'!C4", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },

            # row 5
            # content - Name of Contracting Entity
            'C5:E5': {'value': "='01-summary'!C9", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },
            # label - 3.
            'F5': {'value': '3.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Contract Type
            'G5': {'value': 'Contract Type:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Contract Type
            'H5': {'value': "='01-summary'!C5", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },

            # row 6
            # label - 
            'B6:B7': {'value': '', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Dates
            'C6:C7': {'value': 'Dates:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Start
            'D6': {'value': 'Start:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Start
            'E6': {'value': "='01-summary'!C13", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },
            # label - 4.
            'F6': {'value': '4.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', 'merge': True, },
            # label - Contract value (TEC)
            'G6:G7': {'value': 'Contract value (TEC):', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Contract value (TEC)
            'H6:H7': {'value': "='02-revenue'!C3", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },

            # row 7
            # label - End
            'D7': {'value': 'End:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - End
            'E7': {'value': "='01-summary'!C14", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },

            # row 8
            'B8:H8': {'merge': True},

            # row 9
            # label - Project Title
            'B9:C9': {'value': 'Project Title:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Project Title
            'D9:H9': {'value': "='01-summary'!C3", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },

            # row 10
            # label - Place(s) of Performance
            'B10:C10': {'value': 'Place(s) of Performance:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Place(s) of Performance
            'D10:H10': {'value': "='01-summary'!C7", 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },

            # row 11
            'B11:H11': {'merge': True},


            # row 12
            # label - Scope of Work
            'B12:H12': {'value': 'Scope of Work:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 13
            # content - 06-description
            'B13:H13': {'value': '06-description', 'ws-name-to-link': '06-description', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 14
            'B14:H14': {'merge': True},

            # row 15
            # label - Skills/Expertise Required
            'B15:H15': {'value': 'Skills/Expertise Required:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 16
            # content - 08-technology
            'B16:H16': {'value': '08-technology', 'ws-name-to-link': '08-technology', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 17
            'B17:H17': {'merge': True},

            # row 18
            # label - 6.
            'B18': {'value': '6.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # label - Problems: (If problems encountered on this contract, explain corrective action taken.)
            'C18:H18': {'value': 'Problems: (If problems encountered on this contract, explain corrective action taken.)', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 19
            # content - 11-complexity
            'B19:H19': {'value': '11-complexity', 'ws-name-to-link': '11-complexity', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 20
            'B20:H20': {'merge': True},

            # row 21
            # label - 8.
            'B21': {'value': '8.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # label - Contact Reference: (Name, Telephone Number, E-mail address, and Mailing Address)
            'C21:H21': {'value': 'Contact Reference: (Name, Telephone Number, E-mail address, and Mailing Address)', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },

            # row 22
            # content - 03-contact
            'B22:H22': {'value': '03-contact', 'ws-name-to-link': '03-contact', 'weight': 'normal', 'border-color': '#B7B7B7', 'merge': True, 'note': '{"content": "free"}', },

            # row 23
            'B23:H23': {'merge': True},

            # row 24
            # label - 9.
            'B24': {'value': '9.', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # label - Bidder
            'C24': {'value': 'Bidder:', 'weight': 'bold', 'fgcolor': '#666666', 'bgcolor': '#F3F3F3', 'border-color': '#B7B7B7', },
            # content - Bidder
            'D24:H24': {'value': 'DOER Services Ltd.', 'weight': 'normal', 'fgcolor': '#434343', 'border-color': '#B7B7B7', 'merge': True, },
        },
        'cell-empty-markers': [
            'B3:H5',
            'C3:H7',
            'B9:H10',
            'B12:H13',
            'B15:H16',
            'B18:H19',
            'B21:H22',
            'B24:H24',
        ],
    },
    '01-summary': {
    },
    '02-revenue': {
    },
    '03-contact': {
    },
    '04-joint-venture': {
    },
    '05-people': {
        'num-columns': 4,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left', 'size': 100, 'wrap': True, },
            'B': {'halign': 'left', 'size': 150, 'wrap': True, },
            'C': {'halign': 'left', 'size': 150, 'wrap': True, },
            'D': {'halign': 'left', 'size': 500, 'wrap': True, },
        },
        'review-notes': True,
        'ranges': {
            'A1:Z': {'valign': 'top', 'wrap': True, 'bgcolor': '#FFFFFF', 'border-color': '#B7B7B7', 'no-border': True, },
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left', },
            'A2': {'value': 'review-notes', 'halign': 'left', },
            'B1:C1': {'halign': 'center', },
            'B2:C2': {'value': 'content', 'halign': 'left', 'merge': True, },

            'B2': {'value': 'person'},
            'C2': {'value': 'project-role'},
            'D2': {'value': 'functionalities-performed'},

            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '06-description': {
        'num-columns': 4,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left'  , 'size': 100, },
            'B': {'halign': 'left'  , 'size': 150, },
            'C': {'halign': 'center', 'size':  30, },
            'D': {'halign': 'left'  , 'size': 620, },
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2': {'value': 'header', 'halign': 'left'},
            'C2:D2': {'value': 'narrative-paragraphs', 'halign': 'left', 'merge': True},
            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '07-functionality': {
        'num-columns': 5,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left'  , 'size': 100,  },
            'B': {'halign': 'left'  , 'size': 150,  },
            'C': {'halign': 'center', 'size':  30,  },
            'D': {'halign': 'left'  , 'size': 120,  },
            'E': {'halign': 'left'  , 'size': 500,  },
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2': {'value': 'module', 'halign': 'left'},
            'C2:D2': {'value': 'feature', 'halign': 'left', 'merge': True},
            'E2': {'value': 'process', 'halign': 'left'},
            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '08-technology': {
        'num-columns': 4,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left'  , 'size': 100,  },
            'B': {'halign': 'left'  , 'size': 150,  },
            'C': {'halign': 'center', 'size':  30,  },
            'D': {'halign': 'left'  , 'size': 620,  },
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2': {'value': 'area', 'halign': 'left'},
            'C2:D2': {'value': 'technology-tool', 'halign': 'left', 'merge': True},
            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '09-services': {
        'num-columns': 4,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left'  , 'size': 100,  },
            'B': {'halign': 'left'  , 'size': 150,  },
            'C': {'halign': 'center', 'size':  30,  },
            'D': {'halign': 'left'  , 'size': 620,  },
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2': {'value': 'area', 'halign': 'left'},
            'C2:D2': {'value': 'services-provided-by-staff', 'halign': 'left', 'merge': True},
            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '10-process': {
        'num-columns': 4,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left'  , 'size': 100,  },
            'B': {'halign': 'left'  , 'size': 150,  },
            'C': {'halign': 'center', 'size':  30,  },
            'D': {'halign': 'left'  , 'size': 620,  },
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2': {'value': 'area', 'halign': 'left'},
            'C2:D2': {'value': 'process-description-in-paragraphs-bullets', 'halign': 'left', 'merge': True},
            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '11-complexity': {
        'num-columns': 3,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'halign': 'left', 'size': 100,  },
            'B': {'halign': 'left', 'size': 200,  },
            'C': {'halign': 'left', 'size': 600,  },
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2': {'value': 'project-complexity', 'halign': 'left'},
            'C2': {'value': 'how-it-was-addressed', 'halign': 'left'},
            'B3:Z': {'border-color': '#B7B7B7'},
        },
        'cell-empty-markers': [
            'B3:Z'
        ],
    },
    '12-screenhots': {
    },
    'z-blank': {
    },
    'z-head': {
        'num-columns': 3,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'size': 100, 'halign': 'left', 'wrap': True},
            'B': {'size': 600, 'halign': 'left', 'wrap': True},
            'C': {'size': 200, 'halign': 'right', 'wrap': True},
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2:C2': {'value': 'content', 'merge': True, 'halign': 'left'},
            'B3': {'value': 'Project Datasheet', 'halign': 'left'},
            'C3': {'value': '=image("https://spectrum-bd.biz/data/artifacts/res/logo/spectrum-logo-small-111x89.png", 1)', 'halign': 'right'},
        },
        'cell-empty-markers': [
            'B3:Z',
        ],
    },
    'z-foot': {
        'num-columns': 3,
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'size': 100, 'halign': 'left', 'wrap': True},
            'B': {'size': 600, 'halign': 'left', 'wrap': True},
            'C': {'size': 200, 'halign': 'right', 'wrap': True},
        },
        'review-notes': True,
        'ranges': {
            'A1': {'value': '-toc-new', 'ws-name-to-link': '-toc-new', 'halign': 'left'},
            'A2': {'value': 'review-notes', 'halign': 'left'},
            'B2:C2': {'value': 'content', 'merge': True, 'halign': 'left'},
            'B3': {'value': "='01-summary'!C3", 'halign': 'left'},
            'C3': {'value': 'A', 'note': '{"page-number": "long"}', 'halign': 'right'},
        },
        'cell-empty-markers': [
            'B3:Z',
        ],
    },
}


# Adhoc worksheet structure
WORKSHEET_STRUCTURE_ADHOC = {
    '*': {
        'frozen-rows': 2,
        'frozen-columns': 0,
        'columns': {
            'A': {'size': 100, 'halign': 'left', 'wrap': True, },
        },
    },
}


# which structure we are using
# WORKSHEET_STRUCTURE = WORKSHEET_STRUCTURE_RESUME
WORKSHEET_STRUCTURE = WORKSHEET_STRUCTURE_ADHOC
