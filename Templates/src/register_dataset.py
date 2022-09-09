# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import argparse
from azureml.core import Workspace, Dataset,Datastore

def parse_args():
    parser = argparse.ArgumentParser(description="Register dataset")
    parser.add_argument("-n", type=str, help="Name of the dataset you want to register")
    parser.add_argument("-d", type=str, help="Description of the dataset you want to register")
    parser.add_argument("-t", type=str, help="type of dataset")    
    parser.add_argument("-l", type=str, help="local path of the dataset folder")
    parser.add_argument("-p", type=str, help="Path on data store")
    parser.add_argument("-s", type=str, help="Storage url for cloud storage")
    parser.add_argument("-b", type=str, help="name of blob storage")
    return parser.parse_args()

def main():
    args = parse_args()
    print(args)
    ws = Workspace.from_config()
    datastore_name = args.b
    # datastore = Datastore.get(ws, datastore_name)
    # datastore_paths = [(datastore, args.p)]
    # dataset = Dataset.Tabular.from_delimited_files(path=datastore_paths)
    # dataset = dataset.register(workspace=ws,name=args.n, description=args.d,create_new_version=True)

    if args.t == "local":
        print("local data")
        datastore = Datastore.get(ws, datastore_name)
        # datastore.upload(src_dir = args.l, target_path = args.p, overwrite = True, show_progress = True)
        print(f"About to register dataset {args.n}")

        dataset = Dataset.File.from_files(path=[(datastore, args.p)], validate=True)
        dataset = dataset.register(workspace=ws,name=args.n, description=args.d,create_new_version=True)
        print("Dataset registered")
    else:
        print("cloud_data")
        data_urls = [args.s]
        dataset = Dataset.File.from_files(data_urls)
        dataset = dataset.register(workspace=ws,name=args.n, description=args.d,create_new_version=True)
    

if __name__ == "__main__":
    main()