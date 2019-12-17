FROM python:latest
COPY . .
ENTRYPOINT [ "python",  "merge_list.py" ]
