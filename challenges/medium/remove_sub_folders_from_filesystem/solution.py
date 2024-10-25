from typing import List


class Solution(object):
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        if folders is None:
            return []  # If none was passed in, return an empty list
        elif len(folders) <= 1:
            return folders  # If len is <= 1 then there is nothing left to do

        folders.sort()  # Sort the list lexicographically
        unique_folders = [folders[0]]  # Initialize unique folders with the first element

        # Start iterating the 2nd element
        for i in range(1, len(folders)):
            # Get the previously added unique folder and current folder
            prev = unique_folders[-1] + '/'
            current = folders[i]
            # Check if the current folder starts with the most recent unique folder
            if not f'{current}/'.startswith(prev):
                unique_folders.append(current)  # If not, add it to the unique folders

        return unique_folders
