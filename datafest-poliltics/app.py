import os
import sys

from os import listdir, rename, getcwd
from doctype import DocType

def extract_files_from_folder(path):
    file_texts = {}
    filenames = os.listdir(path)
    for filename in filenames:
        fh = open(path + filename, "r")
        contents = fh.read()
        file_texts[filename] = contents
    return file_texts

def collect_matches_at_threshold(file_texts, doc_types, percentage): # Is it poor form that this method has a side effect of modifying the instance?
    matches_at_percentage = {}
    for doc_type in doc_types:
        matches_at_percentage[doc_type.name] = []
        for filename in file_texts:
            doc_type.identify_file_match(filename, file_texts[filename], percentage)
            if filename in doc_type.matching_files:
                matches_at_percentage[doc_type.name].append(filename)
    return matches_at_percentage

if __name__ == '__main__':

    file_texts_2013 = extract_files_from_folder("../input-data/senate_ocr_text_2013/")
    file_texts_2012 = extract_files_from_folder("../input-data/senate_ocr_text_2012/")

    file_texts = dict(file_texts_2012.items() + file_texts_2013.items())
   
    strings_in_periodic_disclosure = (
        "PERIODIC DISCLOSURE",
        "Report any purchase, sale, or exchange",
        "Include transactions that resulted in a loss",
        "Identification of Assets",
        "IBM Corp. (stock) NYSE",
        "This Periodic Disclosure"
    )

    strings_in_transactions_iv = (
        "PART IV. TRANSACTIONS",
        "See p.3 CONTENTS OF REPORTS Part B",
        "Transaction Date",
    )

    strings_in_publicly_traded = (
        "PART IIIA.",
        "PUBLICLY TRADED ASSETS AND UNEARNED INCOME",
        "Identity of Publicly Traded Assets",
        "And Unearned Income Sources",
        "CONTENTS OF REPORTS Part B",
        "BLOCK C Type and Amount of Income"
    )

    doc_types = (
        DocType("Periodic Disclosure", strings_in_periodic_disclosure),
        DocType("PART IIIA: PUBLICLY TRADED ASSETS AND UNEARNED INCOME SOURCES", strings_in_publicly_traded),
        DocType("PART IV. TRANSACTIONS", strings_in_transactions_iv)
    )

    matches_at_75 = collect_matches_at_threshold(file_texts, doc_types, 0.75)
    matches_at_65 = collect_matches_at_threshold(file_texts, doc_types, 0.65)
    matches_at_50 = collect_matches_at_threshold(file_texts, doc_types, 0.50)


    print "Matches at 75%: "
    print "================="
    for document_type in matches_at_75:
        print document_type + ": " + str(len(matches_at_75[document_type]))
    print "================="
    print "\n"

    print "Matches at 65%: "
    print "================="
    for document_type in matches_at_65:
        print document_type + ": " + str(len(matches_at_65[document_type]))
    print "================="
    print "\n"

    print "Matches at 50%: "
    print "================="
    for document_type in matches_at_50:
        print document_type + ": " + str(len(matches_at_50[document_type]))
    print "================="
    print "\n"

    print "Matches at 65 that aren't in 75:"
    for document_type in matches_at_65:
        print document_type
        for filename in matches_at_65[document_type]:
            if filename not in matches_at_75[document_type]:
               print filename
    
    print "Matches at 50 that aren't in 65:"
    for document_type in matches_at_50:
        print document_type
        for filename in matches_at_50[document_type]:
            if filename not in matches_at_65[document_type]:
               print filename



