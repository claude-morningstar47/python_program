# import os
# from typing import Optional
# import typer


# def find_files_with_extension(directory: str, extension: str) -> list:
#     return [file for file in os.listdir(directory) if file.endswith("." + extension)]


# def delete_file(file: str):
#     try:
#         os.remove(file)
#         print(f"Le fichier '{file}' a été supprimé.")
#     except (FileNotFoundError, OSError) as e:
#         print(f"Erreur lors de la suppression du fichier '{file}': {e}")


# def delete_files(files: list[str]):
#     for file in files:
#         delete_file(file)


# def main(extension: str,
#          directory: Optional[str] = typer.Argument(
#              None, help='Dossier dans lequel chercher.'),
#          delete: bool = typer.Option(
#              False, help='Supprimer les fichiers trouvés.'),
#          file: Optional[str] = typer.Option(
#              None, '--file', '-f', help='Supprimer un fichier spécifique.')
#          ):
#     """
#     Afficher les fichiers trouvés avec l'extension donnée et les supprimer si demandé.
#     """
#     if directory and not os.path.isdir(directory):
#         raise typer.BadParameter(f"Le dossier '{directory}' n'existe pas.")

#     if file:
#         delete_file(file)
#         return

#     files = find_files_with_extension(directory, extension)

#     if files:
#         print(
#             f"Les fichiers avec l'extension '{extension}' dans le dossier '{directory}' sont :")
#         print('\n'.join(files))
#     else:
#         print(
#             f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

#     if delete:
#         delete_files(files)


# if __name__ == "__main__":
#     typer.run(main)


import os
import shutil
import typer
from pathlib import Path


def find_files_with_extension(directory: Path, extension: str) -> list:
    """Retourne une liste des fichiers avec l'extension donnée dans le répertoire donné."""
    return [f.name for f in directory.glob(f"*.{extension}") if f.is_file()]


def delete_file(file: Path) -> bool:
    """Supprime un fichier."""
    try:
        file.unlink()
        print(f"Le fichier '{file}' a été supprimé.")
        return True
    except (FileNotFoundError, OSError) as e:
        print(f"Erreur lors de la suppression du fichier '{file}': {e}")
        return False


def delete_files(files: list[str], confirm: bool = False) -> None:
    """Supprime tous les fichiers de la liste."""
    for file in files:
        path = Path(file)
        if confirm:
            prompt = input(
                f"Voulez-vous supprimer le fichier '{path}' ? [O/n] ")
            if prompt.lower() != "o":
                continue
        delete_file(path)


def main(
    extension: str,
    directory: Path = Path.cwd(),
    delete: bool = False,
    file: Path = None,
    confirm: bool = False,
) -> None:
    """
    Afficher les fichiers trouvés avec l'extension donnée et les supprimer si demandé.

    Args:\n
        extension: L'extension des fichiers à chercher.\n
        directory: Le répertoire dans lequel chercher les fichiers.\n
        delete: Si vrai, supprime les fichiers trouvés sans confirmation.\n
        file: Le fichier à supprimer (ignoré si delete est vrai).\n
        confirm: Si vrai, demande une confirmation avant de supprimer chaque fichier.\n

    Exemple: python mon_programme.py --extension txt --directory /chemin/vers/dossier --delete --confirm

    """
    if file:
        delete_file(file)
        return

    if not directory.is_dir():
        raise typer.BadParameter(f"Le dossier '{directory}' n'existe pas.")

    files = find_files_with_extension(directory, extension)

    if files:
        print(
            f"Les fichiers avec l'extension '{extension}' dans le dossier '{directory}' sont :")
        print('\n'.join(files))
    else:
        print
    (f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

    if delete:
        delete_files(files, confirm)


if __name__ == "__main__":
    typer.run(main)
