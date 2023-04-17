import send2trash
import os
from typing import Optional
import typer


def find_files_with_extension(directory: str, extension: str) -> list:
    return [file for file in os.listdir(directory) if file.endswith("." + extension)]


def delete_file(file: str):
    try:
        os.remove(file)
        print(f"Le fichier '{file}' a été supprimé.")
    except (FileNotFoundError, OSError) as e:
        print(f"Erreur lors de la suppression du fichier '{file}': {e}")


def delete_files(files: list[str]):
    for file in files:
        delete_file(file)


def main(extension: str,
         directory: Optional[str] = typer.Argument(
             None, help='Dossier dans lequel chercher.'),
         delete: bool = typer.Option(
             False, help='Supprimer les fichiers trouvés.'),
         file: Optional[str] = typer.Option(
             None, '--file', '-f', help='Supprimer un fichier spécifique.')
         ):
    """
    Afficher les fichiers trouvés avec l'extension donnée et les supprimer si demandé.
    """
    if directory and not os.path.isdir(directory):
        raise typer.BadParameter(f"Le dossier '{directory}' n'existe pas.")

    if file:
        delete_file(file)
        return

    files = find_files_with_extension(directory, extension)

    if files:
        print(
            f"Les fichiers avec l'extension '{extension}' dans le dossier '{directory}' sont :")
        print('\n'.join(files))
    else:
        print(
            f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

    if delete:
        delete_files(files)


if __name__ == "__main__":
    typer.run(main)
