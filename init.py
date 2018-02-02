import sys
import os

from settings import MASTER_KEY, APPLICATION_ID, REST_API_KEY, PARSE_API_URL

os.environ['PARSE_API_ROOT'] = PARSE_API_URL

from parse_rest.connection import register
from parse_rest.datatypes import Object
from pyexcel_xls import get_data

register(APPLICATION_ID, REST_API_KEY, master=MASTER_KEY)

params = sys.argv


def add_item_to_parse(project_name, keyword, org_name, project_type, category):
    collection = Object.factory(params[1])
    new_item = collection(projectName=project_name, keyword=keyword, orgName=org_name, projType=project_type, category=category)
    return new_item.save()


if __name__ == '__main__':
    file_path = params[2]
    data = get_data(file_path)

    rows = []
    sheet = None
    if data:
        for item in data:
            sheet = data[item]
            break

    if sheet:
        for i, item in enumerate(sheet):
            if i != 0:
                rows.append(dict(project_name=item[4], keyword=str(item[1]), org_name=item[3], project_type=item[0], category=item[2]))

    if rows:
        for counter, row in enumerate(rows):
            print('Importing %s from %s row(s)' % (counter + 1, len(rows)))
            add_item_to_parse(project_name=row.get('project_name'), keyword=row.get('keyword'),
                              org_name=row.get('org_name'), project_type=row.get('project_type'), category=row.get('category'))

