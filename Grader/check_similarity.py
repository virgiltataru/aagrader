import os
import uuid
import mosspy
import shutil
# from pymongo import MongoClient

MOSS_USERID = 535989500

#function to check similarity of all the submissions of a specific hw
#@return a link to a MOSS querry

def check_similarity(mongo, hw_id):
    #create a new directory to store all the files
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)
    #populate files with student names and subbmited code
    # client = MongoClient()

    ans= mongo.db.submissions.find({'assignment_id': int(hw_id)})
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
