import os
import uuid
import mosspy
import shutil

MOSS_USERID = 535989500

#function to check similarity of all the submissions of a specific hw
#@return a link to a MOSS querry
from pymongo import MongoClient

def check_similarity(hw_id):
    #create a new directory to store all the files
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)
    #populate files with student names and subbmited code
    client = MongoClient()
    db = client.submissions
    ans= db.submissions.find({'hw_id': hw_id})
    for a in ans:
        with open(a['Student'] + ".py", 'w+') as f:
            f.write(a['code'])
    #send a MOSS querry and delete the folder with the files afterwards
    m = mosspy.Moss(MOSS_USERID, "python")
    m.addFilesByWildcard("*.py")
    url = m.send()
    os.chdir(current_directory)
    shutil.rmtree(temp_dir, True)
    return url
