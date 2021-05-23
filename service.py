import cv2

from repository.duplicate_collection import DuplicateCollection
from repository.files_collection import FilesCollection


def add_files(files):
    FilesCollection.insert_all(files)


def compare_image(f_file: str, s_file: str):
    image_a = cv2.imread(f_file)
    image_b = cv2.imread(s_file)

    differences = cv2.subtract(image_a, image_b)
    b, q, r = cv2.split(differences)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(q) == 0 and cv2.countNonZero(r) == 0:
        DuplicateCollection.insert(DuplicateCollection.create_duplicate_dict(f_file, s_file))
        print("insert mongo")


def handle_candidate_duplicate_file():
    for results in FilesCollection.get_duplicated_size_and_type():
        results_files = results["results"]
        for res in results_files:
            results_files.remove(res)
            for other_res in results_files:
                print(res['_id'])
                print(other_res['_id'])
                compare_image(res['folder']+"\\\\"+res['file'], other_res['folder']+"\\\\"+other_res['file'])
