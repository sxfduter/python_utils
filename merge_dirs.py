import argparse
import os

def move_merge_dirs(source_root, dest_root):
    for path, dirs, files in os.walk(source_root, topdown=False):
        dest_dir = os.path.join(
            dest_root,
            os.path.relpath(path, source_root)
        )
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for filename in files:
            os.rename(
                os.path.join(path, filename),
                os.path.join(dest_dir, filename)
            )
        for dirname in dirs:
            os.rmdir(os.path.join(path, dirname))
        print("files:{}".format(files))
    os.rmdir(source_root)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Move merge src/* into dest. Overwrite existing files.'
    )
    parser.add_argument('src_dir')
    parser.add_argument('dest_dir')
    args = parser.parse_args()
    move_merge_dirs(args.src_dir, args.dest_dir)
