import os
import sys
import pprint

from os import listdir
from pprint import pprint

from doctype import DocType

def extract_files_from_folder(path):
    file_texts = {}
    filenames = os.listdir(path)
    for filename in filenames:
        fh = open(path + filename, "r")
        contents = fh.read()
        file_texts[filename] = contents
    return file_texts

def get_matches_at_threshold(doctype, percent_threshold):
    matches_at_threshold = 0
    for filename, percent_match in doctype.matching_files.iteritems():
        if percent_match >= percent_threshold:
            matches_at_threshold += 1
    return matches_at_threshold 

if __name__ == '__main__':

    file_texts_2013 = extract_files_from_folder("../input-data/senate_ocr_text_2013/")
    file_texts_2012 = extract_files_from_folder("../input-data/senate_ocr_text_2012/")

    all_files = dict(file_texts_2012.items() + file_texts_2013.items())

    strings_in_primary_form = (
        "UNITED STATES SENATE FINANCIAL",
        "DISCLOSURE REPORT FOR ANNUAL",
        "AND TERMINATION REPORTS",
        "Calendar Year Covered by Report",
        "Senate Office / Agency",
        "ANSWER EACH OF THESE QUESTIONS AND ATTACH THE RELEVANT PART",
        "If Yes, Complete and Attach PART I",
        "make a donation to charity in lieu of paying you for a speech",
        "receive any reportable travel or reimbursements for travel",
        "worth more than $335 from one source",
        "If Yes, Complete and Attach PART II.",
        "Did you hold any reportable positions on or before",
        "receive any reportable gift",
        "If this is your FIRST Report: Did you receive compensation",
        "File this report and any amendments",
        "Secretary of the Senate",
        "Office of Public Records, Room 232",
        "The statement will be made available",
        "to any requesting person",
        "reviewed by the Select Committee on Ethics",
        "subject to civil and criminal sanctions"
    )

    strings_in_ii_earned_income = (
        "PART II. EARNED AND NON-INVESTMENT INCOME",
        "Report the source (name and address)",
        "earned income to you from any source", "aggregating $200 or more",
        "For your spouse, report",
        "earned income which aggregate $1,000",
        "Do not report income from employment",
        "by the U.S. Government",
        "Honoraria Ban:",
        "report honoraria income received",
        "Name of Income Source"
    )

    strings_in_iiia_publicly_traded = (
        "PART IIIA",
        "PUBLICLY TRADED ASSETS", 
        "Identity of Publicly Traded Assets",
        "BLOCK C",
        "Type and Amount of Income",
        "Report the complete name of each publicly traded asset held by",
    )

    strings_in_iiib_non_publicly_traded = (
        "PART IIIB.",
        "NON-PUBLICLY TRADED ASSETS",
        "Identity of Non-Publicly Traded Assets",
        "Report the name, address (city, state and description) of each interest"
    )

    strings_in_iv_transactions = (
        "PART IV. TRANSACTIONS",
        "See p.3 CONTENTS OF REPORTS Part B",
        "Transaction Date",
        "Report any purchase, sale",
        "or exchange by you, your spouse",
        "of any real property, stocks, bonds, commodity futures",
        "amount of the transaction",
        "exceeded $1,000.",
        "Include transactions that resulted in a loss",
        "EXEMPTION TEST"
    )

    strings_in_v_gifts = (
        "Report the source, brief description and value",
        "all gifts aggregating more than $350",
        "received by you, your spouse, or your dependent child",
        "Gifts with a value of $140 or less need not",
        "Exclude: (1) Bequests",
        "Gifts received prior to your Federal employment",
        "Personal hospitality of any individual",
        "meals and beverages unless consumed in connection with a gift of overnight",
        "entertainment provided by a foreign government within",
        "August 12, 201X, Silver platter - Ethics Committee",
        "prohibits most gifts from lobbyists and foreign agents"
    )

    strings_in_vi_reimbursments = (
        "Report necessary travel related expenses",
        "in connection with your provision of services at a speaking engagement, fact-finding event",
        "A description of the itinerary",
        "Report Gifts of travel in Part V.",
        "Example: All States Company",
        "PARI VI. KbIMBURSEMENTS"
    )

    strings_in_vii_liabilities = (
        "PART VII. LIABILITIES",
        "Report liabilities over $10,000 owed by you,",
        "to any one creditor at any time",
        "Exclude: (1) Mortgages on your personal residences",
        "loans secured by automobiles, household furniture",
        "Name of Creditor",
        "First District Bank",
        "EXEMPTION TEST"
    )

    strings_in_viii_postions = (
        "PART VIII. POSITIONS HELD OUTSIDE U.S. GOVERNMENT",
        "Report any positions held by you",
        "whether compensated or not",
        "officer, director, trustee, general partner, proprietor, representative, employee, or consultant",
        "corporation, firm, partnership, or other business enterprise or any non-profit",
        "Exclude: Positions with federal government, religious, social, fraternal",
        "solely of an honorary nature",
        "Name of Organization",
        "Compensation in excess of $200 from any position"
    )

    strings_in_ix_agreements = (
        "AGREEMENTS OR ARRANGEMENTS"
        "Report your agreements or arrangements for future employment",
        "publisher for writing a book",
        "continuing participation in an employee benefit plan",
        "Employment agreement with XYZ Co",
        "Jones & Smith, Hometown, USA",
        "Bethesda, MD"
    )

    strings_in_x_compensation = (
        "PART X. COMPENSATION IN EXCESS OF $5,000",
        "PAID BY ONE SOURCE",
        "FIRST TIME FILERS ONLY:",
        "includes the names of clients and customers of any corporation, firm,"
        "received by you or your business affiliation",
        "names of clients and customers of any corporation",
        "you directly provided the services",
        "need not report the U.S. Government as a source",
        "Brief Description of Duties"
    )

    doctypes = (
        DocType("Primary Form", strings_in_primary_form),
        DocType("Part II Earned Income", strings_in_ii_earned_income),
        DocType("Part IIIa Publicly Traded Assets", strings_in_iiia_publicly_traded),
        DocType("Part IIIb Non-Publicly Traded Assets", strings_in_iiib_non_publicly_traded),
        DocType("Part IV Transactions", strings_in_iv_transactions),
        DocType("Part V Gifts", strings_in_v_gifts),
        DocType("Part VI Reimbursements", strings_in_vi_reimbursments),
        DocType("Part VII Liabilities", strings_in_vii_liabilities),
        DocType("Part VIII Positions", strings_in_viii_postions),
        DocType("Part IX Agreements", strings_in_ix_agreements),
        DocType("Part X Compenstation", strings_in_x_compensation),
    )

    for doctype in doctypes:
        doctype.collect_matches(all_files)

    for doctype in doctypes:
        print doctype.name
        print "Files matching 100% of sample strings: " + str(get_matches_at_threshold(doctype, 1.0))
        print "Files matching 75% of sample strings: " + str(get_matches_at_threshold(doctype, 0.75))
        print "Files matching 65% of sample strings: " + str(get_matches_at_threshold(doctype, 0.65))
        print "Files matching 50% of sample strings: " + str(get_matches_at_threshold(doctype, 0.50))
        print "\n"

    print "Matches at 75%:"
    len_all_files = len(all_files)
    for doctype in doctypes:
            print doctype.name + ": " + str(get_matches_at_threshold(doctype, 0.75))
            pprint(doctype.matching_files)
            len_all_files -= get_matches_at_threshold(doctype, 0.75)
    print "Other: " + str(len_all_files)
    print "All Files: " + str(len(all_files))
    