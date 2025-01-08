#!/usr/bin/env python3

# Resume structure
WORKSHEET_STRUCTURE_RESUME = {
    "00-layout": {
        "num-rows": 29,
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
            "6": {
                "size": 8,
            },
            "9": {
                "size": 8,
            },
            "12": {
                "size": 8,
            },
            "15": {
                "size": 8,
            },
            "18": {
                "size": 8,
            },
            "21": {
                "size": 8,
            },
            "24": {
                "size": 8,
            },
            "27": {
                "size": 8,
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

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "30",
                    "halign": "center",
                },
                "C1": {
                    "value": "250",
                    "halign": "center",
                },
                "D1": {
                    "value": "250",
                    "halign": "center",
                },
                "E1": {
                    "value": "270",
                    "halign": "center",
                },

            # row 2 : column label - review-notes
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                    "bold": True,
                },
                "B2:E2": {
                    "value": "content",
                    "halign": "left",
                    "bold": True,
                    "merge": True,
                },

            # row 3: name of resource
                "B3": {
                    "value": "1",
                    "bold": True,
                },
                "C3": {
                    "value": "NAME OF RESOURCE",
                    "bold": True,
                },
                "D3": {
                    "value": "='01-personal'!D3",
                },
                # photograph
                "E3:E5": {
                    "value": "='01-personal'!E3",
                    "merge": True 
                },

            # row 4: date of birth
                "B4": {
                    "value": "2",
                    "bold": True,
                },
                "C4": {
                    "value": "DATE OF BIRTH",
                    "bold": True,
                },
                "D4": {
                    "value": "='01-personal'!D5",
                },

            # row 5: nationality
                "B5": {
                    "value": "3",
                    "bold": True,
                },
                "C5": {
                    "value": "NATIONALITY",
                    "bold": True,
                },
                "D5": {
                    "value": "='01-personal'!D6",
                },
            
            # row 6: blank
                "B6:I6": {
                    "value": "",
                    "merge": True,
                },

            # row 7: summary of prefessional experience
                "B7": {
                    "value": "4",
                    "bold": True,
                },
                "C7:E7": {
                    "value": "SUMMARY OF PROFESSIONAL EXPERIENCE",
                    "bold": True,
                    "merge": True,
                },

            # row 8: summary of prefessional experience
                "B8:E8": {
                    "value": "02-career-highlight",
                    "ws-name-to-link": "02-career-highlight",
                    "note": '{"content": "free"}',
                    "merge": True,
                },
            
            # row 9: blank
                "B9:I9": {
                    "value": "",
                    "merge": True,
                },

            # row 10: education
                "B10": {
                    "value": "5",
                    "bold": True,
                },
                "C10:E10": {
                    "value": "EDUCATION",
                    "bold": True,
                    "merge": True,
                },

            # row 11: education
                "B11:E11": {
                    "value": "03-education",
                    "ws-name-to-link": "03-education",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 12: blank
                "B12:I12": {
                    "value": "",
                    "note": '{"content": "free", "new-page": true}',
                    "merge": True,
                },

            # row 13: employment record
                "B13": {
                    "value": "6a",
                    "bold": True,
                },
                "C13:E13": {
                    "value": "EMPLOYMENT RECORD",
                    "bold": True,
                    "merge": True,
                },

            # row 14: employment record
                "B14": {
                    "value": "06-job-history",
                    "ws-name-to-link": "06-job-history",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 15: blank
                "B15:I15": {
                    "value": "",
                    "note": '{"content": "free", "new-page": true}',
                    "merge": True,
                },

            # row 16: professional experience
                "B16": {
                    "value": "6b",
                    "bold": True,
                },
                "C16:E16": {
                    "value": "PROFESSIONAL EXPERIENCE",
                    "bold": True,
                    "merge": True,
                },

            # row 17: professional experience
                "B17": {
                    "value": "07-project-roles",
                    "ws-name-to-link": "07-project-roles",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 18: blank
                "B18:I18": {
                    "value": "",
                    "note": '{"content": "free", "new-page": true}',
                    "merge": True,
                },

            # row 19: technical expertise
                "B19": {
                    "value": "7",
                    "bold": True,
                },
                "C19:E19": {
                    "value": "TECHNICAL EXPERTISE",
                    "bold": True,
                    "merge": True,
                },

            # row 20: technical expertise
                "B20": {
                    "value": "05-technical-expertise",
                    "ws-name-to-link": "05-technical-expertise",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 21: blank
                "B21:I21": {
                    "value": "",
                    "merge": True,
                },

            # row 22: professional training
                "B22": {
                    "value": "8a",
                    "bold": True,
                },
                "C22:E22": {
                    "value": "PROFESSIONAL TRAINING",
                    "bold": True,
                    "merge": True,
                },

            # row 23: professional training
                "B23:E23": {
                    "value": "08-training",
                    "ws-name-to-link": "08-training",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 24: blank
                "B24:I24": {
                    "value": "",
                    "merge": True,
                },

            # row 25: professional certificates
                "B25": {
                    "value": "8b",
                    "bold": True,
                },
                "C25:E25": {
                    "value": "PROFESSIONAL CERTIFICATIONS",
                    "bold": True,
                    "merge": True,
                },

            # row 26: professional certificates
                "B26": {
                    "value": "09-certification",
                    "ws-name-to-link": "09-certification",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 27: blank
                "B27:I27": {
                    "value": "",
                    "merge": True,
                },

            # row 28: language proficency
                "B28": {
                    "value": "9",
                    "bold": True,
                },
                "C28:E28": {
                    "value": "LANGUAGES & DEGREE OF PROFICIENCY",
                    "bold": True,
                    "merge": True,
                },

            # row 29: language proficency
                "B29": {
                    "value": "11-language-proficiency",
                    "ws-name-to-link": "11-language-proficiency",
                    "note": '{"content": "free"}',
                    "merge": True,
                },
        },

        "cell-empty-markers": [
            "B3:E5",
        ],
    },

    "00-layout-PS7": {
        "num-rows": 44,
        "num-columns": 9,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "default-row-size": 21,
        "autosize-rows": True,
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
                "size": 40,
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
                "size": 40,
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
                "size": 300,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
        },
        "rows": {
            "7": {
                "size": 8,
            },
            "10": {
                "size": 8,
            },
            "13": {
                "size": 8,
            },
            "16": {
                "size": 8,
            },
            "18": {
                "size": 8,
            },
            "21": {
                "size": 8,
            },
            "23": {
                "size": 8,
            },
            "26": {
                "size": 8,
            },
            "28": {
                "size": 8,
            },
            "31": {
                "size": 8,
            },
        },
        "review-notes": True,
        "ranges": {
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "40",
                    "halign": "center",
                },
                "C1": {
                    "value": "180",
                    "halign": "center",
                },
                "D1": {
                    "value": "50",
                    "halign": "center",
                },
                "E1": {
                    "value": "40",
                    "halign": "center",
                },
                "F1": {
                    "value": "50",
                    "halign": "center",
                },
                "G1": {
                    "value": "40",
                    "halign": "center",
                },
                "H1": {
                    "value": "300",
                    "halign": "center",
                },
                "I1": {
                    "value": "300",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:I2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 7 : blank
                "B7:I7": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 10 : blank
                "B10:I10": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 13 : blank
                "B13:I13": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 16 : blank
                "B16:I16": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 18 : blank
                "B18:I18": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 21 : blank
                "B21:I21": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 23 : blank
                "B23:I23": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 26 : blank
                "B26:I26": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 28 : blank
                "B28:I28": {
                    "value": "",
                    "note": '{"new-page": true, "content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 31 : blank
                "B31:I31": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 33 : blank
                "B33:I33": {
                    "value": "",
                    "merge": True,
                    "no-border": True,
                },

            # row 35 : blank
                "B35:I35": {
                    "value": "",
                    "merge": True,
                    "no-border": True,
                },

            # row 37 : blank
                "B37:I37": {
                    "value": "",
                    "merge": True,
                    "no-border": True,
                },

            # row 3 : proposed position, photograph
                "B3": {
                    "value": "1",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                },
                "C3:G3": {
                    "value": "PROPOSED POSITION FOR THIS PROJECT",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "merge": True,
                },
                "H3": {
                    # "value": "",
                },
                # photograph
                "I3:I6": {
                    "value": "='01-personal'!E3",
                    "halign": "center",
                    "merge": True,
                },

            # row 4 : staff name
                "B4": {
                    "value": "2",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                },
                "C4:G4": {
                    "value": "NAME OF STAFF",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "merge": True,
                },
                "H4": {
                    "value": "='01-personal'!D3",
                },

            # row 5 : date of birth
                "B5": {
                    "value": "3",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                },
                "C5:G5": {
                    "value": "DATE OF BIRTH",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "merge": True,
                },
                "H5": {
                    "value": "='01-personal'!D5",
                },

            # row 6 : nationality
                "B6": {
                    "value": "4",
                    "bgcolor": "#F3F3F3",
                    "bold": True,
                },
                "C6:G6": {
                    "value": "NATIONALITY",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "merge": True,
                },
                "H6": {
                    "value": "='01-personal'!D6",
                },

            # row 3-6 : border around
                "B3:I6": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
                },

            # row 8 : membership
                "B8": {
                    "value": "5",
                    "bold": True,
                },
                "C8:I8": {
                    "value": "MEMBERSHIP IN PROFESSIONAL SOCIETIES",
                    "bold": True,
                    "merge": True,
                },

            # row 9 : membership
                "B9:I9": {
                    "value": "10-membership",
                    "ws-name-to-link": "10-membership",
                    "note": '{"content": "free"}',
                },

            # row 8-9 : border around
                "B8:I9": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 11 : education
                "B11": {
                    "value": "6",
                    "bold": True,
                },
                "C11:I11": {
                    "value": "EDUCATION",
                    "bold": True,
                    "merge": True,
                },

            # row 12 : education
                "B12:I12": {
                    "value": "03-education",
                    "ws-name-to-link": "03-education",
                    "note": '{"content": "free"}',
                },

            # row 11-12 : border around
                "B11:I12": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 14 : training
                "B14": {
                    "value": "7",
                    "bold": True,
                },
                "C14:I14": {
                    "value": "OTHER TRAINING",
                    "bold": True,
                    "merge": True,
                },

            # row 15 : training
                "B15:I15": {
                    "value": "08-training",
                    "ws-name-to-link": "08-training",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 14-15 : border around
                "B14:I15": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 17 : certification
                "B17:I17": {
                    "value": "09-certification",
                    "ws-name-to-link": "09-certification",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 19 : language
                "B19": {
                    "value": "8",
                    "bold": True,
                },
                "C19:I19": {
                    "value": "LANGUAGES & DEGREE OF PROFICIENCY",
                    "bold": True,
                    "merge": True,
                },

            # row 20 : language
                "B20:I20": {
                    "value": "11-language-proficiency",
                    "ws-name-to-link": "11-language-proficiency",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 19-20 : border around
                "B19:I20": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 22 : work countries
                "B22": {
                    "value": "9",
                    "bold": True,
                },
                "C22:G22": {
                    "value": "COUNTRIES OF WORK EXPERIENCE",
                    "bold": True,
                    "merge": True,
                },
                "H22:I22": {
                    "value": "='01-personal'!D13",
                    "merge": True,
                },
                # border around
                "B22:I22": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 24 : employment
                "B24": {
                    "value": "10",
                    "bold": True,
                },
                "C24:I24": {
                    "value": "EMPLOYMENT RECORD",
                    "bold": True,
                    "merge": True,
                },

            # row 25 : employment
                "B25:I25": {
                    "value": "06-job-history",
                    "ws-name-to-link": "06-job-history",
                    "note": '{"content": "free"}',
                },

            # row 24-25 : border around
                "B24:I25": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 27 : project roles
                "B27:I27": {
                    "value": "07-project-roles",
                    "ws-name-to-link": "07-project-roles",
                    "note": '{"content": "free"}',
                },

            # row 29 : work undertaken
                "B29": {
                    "value": "11",
                    "bold": True,
                },
                "C29:I29": {
                    "value": "WORK UNDERTAKEN THAT BEST ILLUSTRATES YOUR CAPABILITY TO HANDLE THIS ASSIGNMENT",
                    "bold": True,
                    "merge": True,
                },

            # row 30 : work undertaken
                "B30:I30": {
                    "value": "02-career-highlight",
                    "ws-name-to-link": "02-career-highlight",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 29-30 : border around
                "B29:I30": {
                    "border-color": "#B7B7B7",
                    "inner-border": False, 
                },

            # row 32 : undertaking
                "B32:I32": {
                    "values": [
                        {   "text": "CERTIFICATION ",
                            "format": {}},
                        {   "text": "[Do not amend this Certification].",
                            "format": {"italic": True}},
                    ],
                    "merge": True,
                },

            # row 34 : undertaking
                "B34:I34": {
                    "value": "I, the undersigned, certify that (i) I was not a former employee of the Client immediately before the submission of this proposal, and (ii) to the best of my knowledge and belief, this bio-data correctly describes myself, my qualifications, and my experience. I understand that any willful misstatement described herein may lead to my disqualification or dismissal, if engaged.",
                    "merge": True,
                    "no-border": True,
                },

            # row 36 : undertaking
                "B36:I36": {
                    "values": [
                        {   "text": "I have been employed by ",
                            "format": {}},
                        {   "text": "='01-personal'!D11",
                            "format": {"bold": True}},
                        {   "text": " continuously for the last twelve (12) months as regular full time staff. Indicate \"Yes\" or \"No\" in the boxes below:",
                            "format": {}},
                    ],
                    "merge": True,
                    "no-border": True,
                },

            # row 38 : Yes/No nd Signature
                "B38:D38": {
                    "value": "Yes",
                    "halign": "right",
                    "merge": True,
                },
                "E38": {
                    "value": "✔",
                    "halign": "center",
                    "border-color": "#B7B7B7",
                },
                "F38": {
                    "value": "No",
                    "halign": "right",
                },
                "G38": {
                    "value": "",
                    "halign": "center",
                    "border-color": "#B7B7B7",
                },
                "H38": {
                    "value": "Signature",
                    "halign": "right",
                },
                "I38:I42": {
                    "value": "='01-personal'!F3",
                    "border-color": "#B7B7B7",
                    "halign": "center",
                    "valign": "middle",
                    "merge": True,
                },

            # row 43 : Date of Signing
                "H43": {
                    "value": "Date of Signing",
                    "halign": "right",
                },
                "I43": {
                    # "value": "",
                    "value": "20 / 06 / 2024",
                    "halign": "center",
                    "border-color": "#B7B7B7",
                },

            # row 44 : Day Format
                "I44": {
                    "value": "Day / Month / Year",
                    "halign": "center",
                },
        },

        "cell-empty-markers": [
            "B3:I5",
            "B8:I9",
            "B11:I12",
            "B14:I15",
            "B19:I20",
            "B22:I22",
            "B24:I25",
            "B27:I27",
            "B32:I32",
            "B29:I30",
            "B32:I32",
            "B34:I34",
            "B36:I36",
            "D38:F38",
            "H38",
            "I38:I42",
            "H43:I43",
            "I44",
        ],
    },

    "01-personal": {
        "num-rows": 14,
        "num-columns": 6,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "default-row-size": 21,
        "autosize-rows": True,
        "columns": {
            "A": {"size": 100, "halign": "left", "wrap": True},
            "B": {"size": 30, "halign": "center", "wrap": True},
            "C": {"size": 140, "halign": "left", "wrap": True},
            "D": {"size": 230, "halign": "left", "wrap": True},
            "E": {"size": 250, "halign": "center", "wrap": True},
            "F": {"size": 150, "halign": "center", "wrap": True},
        },
        "review-notes": True,
        "ranges": {
            # full worksheet
                "A1:Z": {
                    "font-family": "Arial",
                    "font-size": 10,
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                    "bold": False,
                },
                "B1": {
                    "value": "30",
                    "halign": "center",
                    "bold": False,
                },
                "C1": {
                    "value": "140",
                    "halign": "center",
                    "bold": False,
                },
                "D1": {
                    "value": "230",
                    "halign": "center",
                    "bold": False,
                },
                "E1": {
                    "value": "250",
                    "halign": "center",
                    "bold": False,
                },
                "F1": {
                    "value": "150",
                    "halign": "center",
                    "bold": False,
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                    "bold": True,
                },
                "B2:F2": {
                    "value": "content",
                    "halign": "left",
                    "bold": True,
                    "merge": True,
                },

            # row 3 : name. photo, signature
                "B3": {
                    "value": "1",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "center",
                },
                "C3": {
                    "value": "Name",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "D3": {
                    "bold": False,
                    "halign": "left",
                },
                "E3:E14": {
                    "bold": False,
                    "halign": "center",
                    "valign": "middle",
                    "merge": True,
                },
                "F3:F14": {
                    "bold": False,
                    "halign": "center",
                    "valign": "middle",
                    "merge": True,
                },

            # B3:F : border around  
                "B3:F": {
                    "border-color": "#B7B7B7",
                    "inner-border": True,
                },
        },
        "cell-empty-markers": ["B3:F"],
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "150",
                    "halign": "center",
                },
                "C1": {
                    "value": "30",
                    "halign": "center",
                },
                "D1": {
                    "value": "620",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:D2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3-end : border around
                "B3:D": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "80",
                    "halign": "center",
                },
                "C1": {
                    "value": "210",
                    "halign": "center",
                },
                "D1": {
                    "value": "210",
                    "halign": "center",
                },
                "E1": {
                    "value": "300",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:E2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Year",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "Degree",
                },
                "D3": {
                    "value": "Subject/Discipline",
                },
                "E3": {
                    "value": "Institute",
                },

            # row 3-end : border around
                "B3:E": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "170",
                    "halign": "center",
                },
                "C1": {
                    "value": "30",
                    "halign": "center",
                },
                "D1": {
                    "value": "600",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:D2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Area",
                    "note": '{"repeat-rows": 1}',
                },
                "C3:D3": {
                    "value": "Expertise",
                    "halign": "left",
                    "merge": True,
                },

            # row 3-end : border around
                "B3:D": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "170",
                    "halign": "center",
                },
                "C1": {
                    "value": "30",
                    "halign": "center",
                },
                "D1": {
                    "value": "600",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:D2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Area",
                    "note": '{"repeat-rows": 1}',
                },
                "C3:D3": {
                    "value": "Expertise",
                    "halign": "left",
                    "merge": True,
                },

            # row 3-end : border around
                "B3:D": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "60",
                    "halign": "center",
                },
                "C1": {
                    "value": "60",
                    "halign": "center",
                },
                "D1": {
                    "value": "30",
                    "halign": "center",
                },
                "E1": {
                    "value": "650",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:E2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "From",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "To",
                },
                "D3:E3": {
                    "value": "Employment History",
                    "merge": True,
                },

            # row 3-end : border around
                "B3:E": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
                },
        },
        "cell-empty-markers": [
            "B3:Z",
        ],
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "60",
                    "halign": "center",
                },
                "C1": {
                    "value": "60",
                    "halign": "center",
                },
                "D1": {
                    "value": "30",
                    "halign": "center",
                },
                "E1": {
                    "value": "650",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:E2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "From",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "To",
                },
                "D3:E3": {
                    "value": "Company/Project/Position/ Relevant Technical and Management Experience",
                    "merge": True,
                },

            # row 3-end : border around
                "B3:E": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "80",
                    "halign": "center",
                },
                "C1": {
                    "value": "450",
                    "halign": "center",
                },
                "D1": {
                    "value": "370",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:D2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Year",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "Training",
                },
                "D3": {
                    "value": "Institute",
                },

            # row 3-end : border around
                "B3:D": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "70",
                    "halign": "center",
                },
                "C1": {
                    "value": "150",
                    "halign": "center",
                },
                "D1": {
                    "value": "280",
                    "halign": "center",
                },
                "E1": {
                    "value": "300",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:E2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Year",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "Vendor/ OEM/ Subject",
                },
                "D3": {
                    "value": "Certification",
                },
                "E3": {
                    "value": "Details",
                },

            # row 3-end : border around
                "B3:E": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "250",
                    "halign": "center",
                },
                "C1": {
                    "value": "150",
                    "halign": "center",
                },
                "D1": {
                    "value": "125",
                    "halign": "center",
                },
                "E1": {
                    "value": "125",
                    "halign": "center",
                },
                "F1": {
                    "value": "150",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:F2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Professional Organization/ Society",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "Membership Rank/ Level",
                },
                "D3": {
                    "value": "Membership ID/ Number",
                },
                "E3": {
                    "value": "Member Since",
                },
                "F3": {
                    "value": "Details",
                },

            # row 3-end : border around
                "B3:F": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "110",
                    "halign": "center",
                },
                "C1": {
                    "value": "230",
                    "halign": "center",
                },
                "D1": {
                    "value": "230",
                    "halign": "center",
                },
                "E1": {
                    "value": "230",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:E2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Language",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "Speaking",
                },
                "D3": {
                    "value": "Reading",
                },
                "E3": {
                    "value": "Writing",
                },

            # row 3-end : border around
                "B3:E": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "200",
                    "halign": "center",
                },
                "C1": {
                    "value": "600",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:C2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3-end : border around
                "B3:C": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
                },
        },
        "cell-empty-markers": [
            "B3:C",
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
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "140",
                    "halign": "center",
                },
                "C1": {
                    "value": "150",
                    "halign": "center",
                },
                "D1": {
                    "value": "190",
                    "halign": "center",
                },
                "E1": {
                    "value": "190",
                    "halign": "center",
                },
                "F1": {
                    "value": "130",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
                "B2:F2": {
                    "value": "content",
                    "halign": "left",
                    "merge": True,
                },

            # row 3 : column headers
                "B3": {
                    "value": "Name",
                    "note": '{"repeat-rows": 1}',
                },
                "C3": {
                    "value": "Position",
                },
                "D3": {
                    "value": "Company",
                },
                "E3": {
                    "value": "Email",
                },
                "F3": {
                    "value": "Phone Number",
                },

            # row 3-end : border around
                "B3:F": {
                    "border-color": "#B7B7B7",
                    "inner-border": True, 
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


# PDS structure
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

    "00-layout-PS7": {
        "num-rows": 41,
        "num-columns": 4,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "default-row-size": 21,
        "autosize-rows": True,
        "columns": {
            "A": {
                "size": 100,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "B": {
                "size": 240,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "C": {
                "size": 240,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "D": {
                "size": 320,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
        },
        "rows": {
            "15": {
                "size": 8,
            },
            "18": {
                "size": 8,
            },
            "21": {
                "size": 8,
            },
            "25": {
                "size": 8,
            },
            "28": {
                "size": 8,
            },
            "31": {
                "size": 8,
            },
            "35": {
                "size": 8,
            },
        },
        "review-notes": True,
        "ranges": {
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "no-border": True,
                    "bold": False,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "B1": {
                    "value": "240",
                    "halign": "center",
                },
                "C1": {
                    "value": "240",
                    "halign": "center",
                },
                "D1": {
                    "value": "320",
                    "halign": "center",
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                    "bold": True,
                },
                "B2:D2": {
                    "value": "content",
                    "halign": "left",
                    "bold": True,
                    "merge": True,
                },

            # row 3 : assignment name, approximate value
                "B3:C3": {
                    "value": "Assignment Name:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                    "merge": True,
                },
                "D3": {
                    "value": "Approx value of the Contract (Tk. Lacs):",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },

            # row 4 : assignment name, approximate value
                "B4:C4": {
                    "value": "='01-summary'!C3",
                    "halign": "left",
                    "merge": True,
                },
                "D4": {
                    "value": "='02-revenue'!C3",
                    "halign": "left",
                },

            # row 5 : Country and Duration of assignment (months):
                "B5:C5": {
                    "value": "Country:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                    "merge": True,
                },
                "D5": {
                    "value": "Duration of assignment (months):",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },

            # row 6 : Country and Duration of assignment (months):
                "B6:C6": {
                    "value": "='01-summary'!C6",
                    "halign": "left",
                    "merge": True,
                },
                "D6:D8": {
                    "value": "='01-summary'!C8",
                    "halign": "left",
                },

            # row 7 : Location within country:
                "B7:C7": {
                    "value": "Location within country:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                    "merge": True,
                },

            # row 8 : Location within country:
                "B8:C8": {
                    "value": "='01-summary'!C7",
                    "halign": "left",
                    "merge": True,
                },

            # row 9 : Client and Total No of staff-month of the assignment:
                "B9:C9": {
                    "value": "Name of Client:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                    "merge": True,
                },
                "D9": {
                    "value": "Total No of staff-month of the assignment:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },

            # row 10 : Client and Total No of staff-month of the assignment:
                "B10:C10": {
                    "value": "='01-summary'!C9",
                    "halign": "left",
                    "merge": True,
                },
                "D10:D12": {
                    "value": "='01-summary'!C12",
                    "halign": "left",
                },

            # row 11 : Address:
                "B11:C11": {
                    "value": "Address:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                    "merge": True,
                },

            # row 12 : Address
                "B12:C12": {
                    "value": "='01-summary'!C10",
                    "halign": "left",
                    "note": '{"keep-line-breaks": true}',
                    "merge": True,
                },

            # row 13 : Start/End Date and Approx value of services provided by your firm under the contract (Tk. Lacs):
                "B13": {
                    "value": "Start Date (Month/Year):",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C13": {
                    "value": "Completion Date (Month/Year):",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "D13": {
                    "value": "Approx value of services provided by your firm under the contract (Tk. Lacs):",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },

            # row 14 : Start/End Date and Approx value of services provided by your firm under the contract (Tk. Lacs):
                "B14": {
                    "value": "='01-summary'!C13",
                    "halign": "left",
                },
                "C14": {
                    "value": "='01-summary'!C14",
                    "halign": "left",
                },
                "D14": {
                    "value": "='02-revenue'!C3",
                    "halign": "left",
                },

            # row 15 : blank
                "B15:D15": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 16 : joint venture
                "B16:C16": {
                    "value": "Name of Joint Venture/Associated Consultants, if any:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "merge": True,
                },
                "D16": {
                    "value": "No of Staff-Months of Key professional staff provided by Joint Venture/Associated Consultants:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                },

            # row 17 : joint venture
                "B17:D17": {
                    "value": "04-joint-venture",
                    "ws-name-to-link": "04-joint-venture",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 18 : blank
                "B18:D18": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 19 : Name of senior professional staff (Project Director/Coordinator, Team Leader) Involved and Functions Performed:
                "B19:D19": {
                    "value": "Name of senior professional staff (Project Director/Coordinator, Team Leader) Involved and Functions Performed:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 20 : Name of senior professional staff (Project Director/Coordinator, Team Leader) Involved and Functions Performed:
                "B20:D20": {
                    "value": "05-people",
                    "ws-name-to-link": "05-people",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 21 : blank
                "B21:D21": {
                    "value": "",
                    "note": '{"content": "free", "new-page": true}',
                    "merge": True,
                    "no-border": True,
                },

            # row 22 : Narrative description of Project
                "B22:D22": {
                    "value": "Narrative description of Project:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 23 : Project Description
                "B23:D23": {
                    "value": "Project Description",
                    "bold": True,
                    "italic": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "merge": True,
                },

            # row 24 : Project Description
                "B24:D24": {
                    "value": "06-description",
                    "ws-name-to-link": "06-description",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 25 : blank
                "B25:D25": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 26 : Functionality
                "B26:D26": {
                    "value": "Functionality",
                    "bold": True,
                    "italic": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 27 : Functionality
                "B27:D27": {
                    "value": "07-functionality",
                    "ws-name-to-link": "07-functionality",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 28 : blank
                "B28:D28": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 29 : Technology
                "B29:D29": {
                    "value": "Technology",
                    "bold": True,
                    "italic": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 30 : Technology
                "B30:D30": {
                    "value": "08-technology",
                    "ws-name-to-link": "08-technology",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 31 : blank
                "B31:D31": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 32 : Description of actual services provided by your Staff
                "B32:D32": {
                    "value": "Description of actual services provided by your Staff:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 33 : Services Provided
                "B33:D33": {
                    "value": "Services Provided",
                    "bold": True,
                    "italic": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 34 : Services Provided
                "B34:D34": {
                    "value": "09-services",
                    "ws-name-to-link": "09-services",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 35 : blank
                "B35:D35": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 36 : Processes Adopted
                "B36:D36": {
                    "value": "Processes Adopted",
                    "bold": True,
                    "italic": True,
                    "bgcolor": "#F3F3F3",
                    "border-color": "#B7B7B7",
                    "halign": "left",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 37 : Processes Adopted
                "B37:D37": {
                    "value": "10-process",
                    "ws-name-to-link": "10-process",
                    "note": '{"content": "free"}',
                    "merge": True,
                },

            # row 38 : blank
                "B38:D38": {
                    "value": "",
                    "note": '{"content": "free"}',
                    "merge": True,
                    "no-border": True,
                },

            # row 39 : Firm’s Name
                "B39": {
                    "value": "Firm’s Name:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C39:D39": {
                    "value": "='01-summary'!C21",
                    "merge": True,
                },

            # row 40-41 : Authorised Signature
                "B40:B41": {
                    "value": "Authorised Signature:",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                    "merge": True,
                },
                "C40:D41": {
                    # "value": "",
                    "merge": True,
                },

            # B3:D14 : border around and inner
                "B3:D14": {
                    "border-color": "#B7B7B7",
                    "no-border": False,
                    "inner-border": True,
                },

            # B39:D41 : border around and inner
                "B39:D41": {
                    "border-color": "#B7B7B7",
                    "no-border": False,
                    "inner-border": True,
                },

        },
        "cell-empty-markers": [
            "B4:D14",
            "C39:D39",
            "C40:D41",
        ],
    },

    '01-summary': {
        "num-rows": 21,
        "num-columns": 3,
        "frozen-rows": 2,
        "frozen-columns": 0,
        "default-row-size": 21,
        "autosize-rows": True,
        "columns": {
            "A": {
                "size": 100,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "B": {
                "size": 300,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
            "C": {
                "size": 500,
                "halign": "left",
                "valign": "top",
                "wrap": True,
            },
        },
        "review-notes": True,
        "ranges": {
            # full worksheet
                "A1:Z": {
                    "valign": "top",
                    "wrap": True,
                    "bgcolor": "#FFFFFF",
                    "border-color": "#B7B7B7",
                    "bold": False,
                    "no-border": True,
                },

            # row 1 : -toc-new and column sizes
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                    "bold": False,
                },
                "B1": {
                    "value": "300",
                    "halign": "center",
                    "bold": False,
                },
                "C1": {
                    "value": "500",
                    "halign": "center",
                    "bold": False,
                },

            # row 2 : review-notes and column labels
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                    "bold": True,
                },
                "B2:C2": {
                    "value": "content",
                    "halign": "left",
                    "bold": True,
                    "merge": True,
                },

            # row 3 : Assignment Name
                "B3": {
                    "value": "Assignment Name",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C3": {
                    "halign": "left",
                    "bold": False,
                },

            # row 4 : Contract No.
                "B4": {
                    "value": "Contract No.",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C4": {
                    "halign": "left",
                    "bold": False,
                },

            # row 5 : Contract Type
                "B5": {
                    "value": "Contract Type",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C5": {
                    "halign": "left",
                    "bold": False,
                },

            # row 6 : Country
                "B6": {
                    "value": "Country",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C6": {
                    "halign": "left",
                    "bold": False,
                },

            # row 7 : Assignment Location within Country
                "B7": {
                    "value": "Assignment Location within Country",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C7": {
                    "halign": "left",
                    "bold": False,
                },

            # row 8 : Duration of Assignment (months)
                "B8": {
                    "value": "Duration of Assignment (months)",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C8": {
                    "halign": "left",
                    "bold": False,
                },

            # row 9 : Name of Client
                "B9": {
                    "value": "Name of Client",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C9": {
                    "halign": "left",
                    "bold": False,
                },

            # row 10 : Address
                "B10": {
                    "value": "Address",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C10": {
                    "halign": "left",
                    "bold": False,
                },

            # row 11: Professional Staff Count
                "B11": {
                    "value": "Professional Staff Count",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C11": {
                    "halign": "left",
                    "bold": False,
                },

            # row 12 : Professional Staff-Months
                "B12": {
                    "value": "Professional Staff-Months",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C12": {
                    "halign": "left",
                    "bold": False,
                },

            # row 13 : Start Date
                "B13": {
                    "value": "Start Date",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C13": {
                    "halign": "left",
                    "date-format": "Mmm/YYYY",
                    "bold": False,
                },

            # row 14 : Completion Date
                "B14": {
                    "value": "Completion Date",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C14": {
                    "halign": "left",
                    "date-format": "Mmm/YYYY",
                    "bold": False,
                },

            # row 15 : Live URL
                "B15": {
                    "value": "Live URL",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C15": {
                    "halign": "left",
                    "bold": False,
                },

            # row 16 : Demo URL
                "B16": {
                    "value": "Demo URL",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C16": {
                    "halign": "left",
                    "bold": False,
                },

            # row 17 : Is Joint Venture?
                "B17": {
                    "value": "Is Joint Venture?",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C17": {
                    "halign": "center",
                    "checkbox": True,
                    "bold": False,
                },

            # row 18 : Screenshot Available?
                "B18": {
                    "value": "Screenshot Available?",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C18": {
                    "halign": "center",
                    "checkbox": True,
                    "bold": False,
                },

            # row 19 : WCC Available?
                "B19": {
                    "value": "WCC Available?",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C19": {
                    "halign": "center",
                    "checkbox": True,
                    "bold": False,
                },

            # row 20 : WO/PO Available?
                "B20": {
                    "value": "WO/PO Available?",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C20": {
                    "halign": "center",
                    "checkbox": True,
                    "bold": False,
                },

            # row 21 : Organization Name
                "B21": {
                    "value": "Organization Name",
                    "bold": True,
                    "bgcolor": "#F3F3F3",
                    "halign": "left",
                },
                "C21": {
                    "halign": "left",
                    "checkbox": False,
                    "bold": False,
                },
        },
        "cell-empty-markers": [
            "C3:C21",
        ],
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
        'review-notes': True,
        "ranges": {
                "A1": {
                    "value": "-toc-new",
                    "ws-name-to-link": "-toc-new",
                    "halign": "left",
                },
                "A2": {
                    "value": "review-notes",
                    "halign": "left",
                },
        },
    },
}


# which structure we are using
WORKSHEET_STRUCTURE = WORKSHEET_STRUCTURE_RESUME
# WORKSHEET_STRUCTURE = WORKSHEET_STRUCTURE_PDS
# WORKSHEET_STRUCTURE = WORKSHEET_STRUCTURE_ADHOC
