import os
import shutil
import argparse


def copy_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        try:
            if os.path.isfile(item_path):
                _, extension = os.path.splitext(item)
                extension = extension[1:] if extension else 'no_ext'

                extension_dir = os.path.join(dest_dir, extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                shutil.copy(item_path, os.path.join(extension_dir, item))

            elif os.path.isdir(item_path):
                copy_files(item_path, dest_dir)
        except PermissionError:
            print(f"Доступ за шляхом {item_path} закритий.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Додаток для рекурсивного копіюваня файлів')
    parser.add_argument('source', help='Шлях до вихідної директорії для рекурсивного копіюваня файлів')
    parser.add_argument('dest', nargs='?', default='dist', help='Шлях до директорії куди буде кпіювання (за змовчуванням: dist)')

    try:
        args = parser.parse_args()
        source_directory = args.source

        destination_directory = args.dest

        copy_files(source_directory, destination_directory)
    except SystemExit: # Не потрібно нічого робити, argparse вже вивів повідомлення про помилку
        pass
