import os
import uuid
import mosspy

MOSS_USERID = 535989500

def check_similarity(hw_id):
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)

    ans= mongo.db.submissions.find({"hw_id": hw_id})
    for a in ans:
        with open(a['Student'] + ".py", 'w+') as f:
            f.write(a['code'])

    m = mosspy.Moss(MOSS_USERID, "python")
    m.addFilesByWildcard("*.py")
    url = m.send()
    os.chdir(current_directory)
    shutil.rmtree(temp_dir, True)
    return url
