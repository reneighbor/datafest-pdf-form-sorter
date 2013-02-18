PDF Form-Sorter
========================

Take scanned documents and organize them by common strings. Useful for categorizing files that came from scanned files.

Example:
        strings_in_v_gifts =  (
            "Report the source",
            "description and value",
            "aggregating more than $350",
            "value of $140"
        )
        part_v_gifts = DocType("Part V: Gifts", strings_in_v_gifts)

        filename_0 = "file_0"
        filetext_0 = "Report the source, brief description and value of all gifts aggregating more than $350 in value received by you, your spouse, or your dependent child, (See p.3 CONTENTS OF REPORTS Part B of Instructions), from each source. Gifts with a value of $140 or less need not be aggregated towards the disclosure threshold."

        filename_0 = "file_1"
        filetext_0 = "Identity of Non-Publldy Traded Assets and Unearned Income Sources
        Report the name, address (dty, state and description) of each Interest held by you, your spouse, or your dependent child (See pA CONTENTS OF REPORTS Part B of Instructions) for the production of income or investment in a non-ouflto trade or business which:
        (1) had a value exceeding $1,000 at the dose of the reporting period; and/or
        (2) generated over $200 in 'unearned" Income during the reporting period."
                

        all_files = {
            "filename_0": filetext_0,
            "filename_1": filetext_1
        }
        part_v_gifts.identify_file_match(filename, filetext)

        pprint part_v_gifts.matching_files
        >> {'file_0': 1}


This tool was written as part of the February 2013 [BiCoastal Datafest](http://www.bdatafest.computationalreporting.com/) at Stanford University. Our team was led by Marc Joffee of Public Sector Credit Solutions and Fergus Pitt from Columbia Journalism School.