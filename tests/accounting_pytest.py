import os
import accounting
import requests
from accounting import check_document_existance, get_doc_owner_name, \
    get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, \
    append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_document_info, show_all_docs_info, add_new_doc



class TestFunc:
    def test_check_document_existance(self):
        result = check_document_existance("11-2")
        assert result == True

    def test_get_doc_owner_name(self):
        result = get_doc_owner_name("10006")
        assert result == "Аристарх Павлов"

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf('2207 876234')
        assert '2207 876234' not in main.directories["1"]

    def test_add_new_shelf(self):
        add_new_shelf("4")
        assert "4" in main.directories.keys()

    def test_append_doc_to_shelf(self):
        append_doc_to_shelf("111", "6")
        assert '111' in main.directories["6"]

    def test_delete_doc(self):
        delete_doc("11-2")
        assert "11-2" not in [el["number"] for el in main.documents] and\
               "11-2" not in [val for val in main.directories.values()]

    def test_get_doc_shelf(self):
        result = get_doc_shelf("10006")
        assert result == "2"

    def test_move_doc_to_shelf(self):
        move_doc_to_shelf("2207 876234", "3")
        assert "2207 876234" not in main.directories["1"] and "2207 876234" in main.directories["3"]

    def test_show_document_info(self):
        show_document_info({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})
        assert "passport, 2207 876234 Василий Гупкин"

    def test_add_new_doc(self):
        add_new_doc("2002 543821", "passport", "Мухаммед Али", "3")
        doc = {"type": "passport", "number": "2002 543821", "name": "Мухаммед Али"}
        assert doc in main.documents and "2002 543821" in main.directories["3"]






