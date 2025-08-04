We will quickly review all of them for understanding:


1. Filesystem & Paths

os can be used for other things as well, but they have better alternatives, it shines the best in File handling

Basic Ops:
1. os.getcwd(): 
   `os.getcwd()` → Returns **current working directory**.

   * Always returns an **absolute path**.
   * It’s **where your script is being *run*** from, not where it’s saved.

   ```python
   print(os.getcwd())  # e.g., C:\Users\victo\...
   ```

   Use `os.chdir()` to change it.

2. os.chdir(path):
   `os.chdir(path)` changes the working dir *for the current process only*.

   * Affects relative path operations after that.
   * If the path doesn't exist: `FileNotFoundError`.
   * Works with `..`, `.`, and absolute/relative paths.

   ```python
   os.chdir("..")  # Go up one directory
   ```

   Changing cwd *doesn't persist* after the script ends.

3. os.listdir(path='.'):
    `os.listdir(path='.')` → Returns a **list of names** (files + folders) in a directory.

    * Default is current directory.
    * Doesn’t recurse. so just the current directory content are listed.
    * Hidden files are included on Linux, not on Windows.

    ```python
    os.listdir(".")  # ['file.txt', 'folder', '.hidden']
    ```

    Use with `os.path.isdir()` / `isfile()` to filter.

    Misonception: chdir() changes cwd, so naturally it would affect listdir() through that prespective.

4. os.makedirs(path):
   
    `os.mkdir(path)` → Makes **one** directory.

   * Fails if parent dirs don’t exist.
   * Throws `FileExistsError` if it already exists.

   ```python
   os.mkdir("raccoon")  # Works only if CWD exists and raccoon doesn’t
   ```


   `os.makedirs(path)` → Makes **all needed parent dirs**. (= it is recursive)

   ```python
   os.makedirs("raccoon/nest/bed")  # Creates full path
   ```

   Add `exist_ok=True` to avoid error if already exists.

   ```python
   os.makedirs("raccoon", exist_ok=True)
   ```

5. remove(file):
   * `os.remove(path)` → Deletes a **file**, not folders.
     Errors if file doesn’t exist or path is a directory.

   ```python
   os.remove("trash.txt")
   ```

   * `os.rmdir(path)` → Deletes an **empty directory**.
     Throws `OSError` if it's not empty.

   ```python
   os.rmdir("empty_folder")
   ```

   ---

   * `shutil.rmtree(path)` → **Recursively deletes** entire folder trees (be careful).
     Use this if you want `rm -rf` vibes.

   ```python
   import shutil
   shutil.rmtree("full_folder")
   ```

6. `os.rename(src, dst)` and `os.replace(src, dst)`:

    `os.rename(src, dst)` → Renames or moves a file/folder.

    * Fails if `dst` exists (on Windows).
    * Moves across folders if `dst` is a path.

    ```python
    os.rename("old.txt", "new.txt")
    os.rename("file.txt", "subdir/file.txt")
    ```

    ---

    `os.replace(src, dst)` → Same as `rename`, **but overwrites** if `dst` exists.

    * Safer if you *want* to overwrite.
    * Works atomically on most OSes (less race conditions).

    ```python
    os.replace("file.txt", "existing.txt")  # Overwrites existing.txt
    ```

    `rename()` = cautious
    `replace()` = aggressive

7. os.stat():
    Now, `os.stat(path)` is your **file metadata spell**—gives you *everything* about a file: size, permissions, timestamps, and more.

    ```python
    import os

    stats = os.stat("example.txt")
    ```

    You get a `stat_result` object with fields like:

    * `st_size` → size in **bytes**
    * `st_mtime` → **modification time** (timestamp)
    * `st_ctime` → **creation time** (Windows) or metadata change (Unix)
    * `st_atime` → **last access time**
    * `st_mode` → permission bits
    * `st_ino` → inode number (Unix)
    * `st_uid`, `st_gid` → owner info (Unix)


