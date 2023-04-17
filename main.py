

import send2trash
import os
from typing import Optional
import typer

# Fonction de recherche de fichiers avec une extension donnée dans un dossier


def find_files_with_extension(directory: str, extension: str) -> list:
    files = []
    for file in os.listdir(directory):
        if file.endswith("." + extension):
            files.append(file)
    return files


# Fonction de suppression des fichiers trouvés
def delete_files(files: list[str]):
    for file in files:
        try:
            os.remove(f'"{file}"')
            print(f'Le fichier {file} a été supprimé.')
        except FileNotFoundError:
            print(f'Le fichier {file} n\'existe pas.')
        except OSError as e:
            print(f'Erreur lors de la suppression du fichier {file} : {e}')


def delete_file(file: str):
    try:
        os.remove(file)
        print(f"Le fichier '{file}' a été supprimé.")
    except FileNotFoundError:
        print(f"Le fichier '{file}' n'existe pas.")
    except OSError as e:
        print(f"Erreur lors de la suppression du fichier '{file}' : {e}")


# Définition de la fonction principale


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
    # Vérification de la validité du dossier donné
    if not os.path.isdir(directory):
        raise typer.BadParameter(f"Le dossier '{directory}' n'existe pas.")

    # Si un fichier spécifique est donné, supprime ce fichier et quitte la fonction
    if file:
        delete_file(file)
        return

    # Recherche des fichiers avec l'extension donnée dans le dossier
    files = find_files_with_extension(directory, extension)

    # Affichage des fichiers trouvés
    if len(files) > 0:
        print(
            f"Les fichiers avec l'extension '{extension}' dans le dossier '{directory}' sont :")
        for file in files:
            print(file)
    else:
        print(
            f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

    # Suppression des fichiers trouvés si l'option "delete" est activée
    if delete:
        delete_files(files)


# Condition pour exécuter le script uniquement si c'est le fichier principal
if __name__ == "__main__":
    # Appel de la fonction principale via la bibliothèque "typer"
    typer.run(main)
