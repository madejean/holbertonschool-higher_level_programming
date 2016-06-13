import sys
import peewee
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from models import *

if len(sys.argv) < 2:
    print "Please enter an action"

elif (sys.argv[1] == "create"):
        try:
            School.create_table()
        except peewee.OperationalError:
            pass
        try:
            Batch.create_table()
        except peewee.OperationalError:
            pass
        try:
            User.create_table()
        except peewee.OperationalError:
            pass
        try:
            Student.create_table()
        except peewee.OperationalError:
            pass
        try:
            Exercise.create_table()
        except peewee.OperationalError:
            pass

elif (sys.argv[1] == "print"):
    if len(sys.argv) < 3:
        pass
    else:
        if sys.argv[2] == "school":
            for s in School.select():
                print s
        elif sys.argv[2] == "batch":
            for b in Batch.select():
                print b
        elif sys.argv[2] == "user":
            for u in Users.select():
                print u
        elif sys.argv[2] == "student":
            for student in Student.select():
                print student
        elif sys.argv[2] == "exercise":
            for exercises in Exercise.select():
                print exercises

elif (sys.argv[1] == "insert"):
    if len(sys.argv) < 3:
        pass
    else:
        if sys.argv[2] == "school":
            S = School.create(name = sys.argv[3])
            print "New school: " + str(S)
        elif sys.argv[2] == "batch":
            b = Batch.create(
                school_id = sys.argv[3],
                name = sys.argv[4]
            )
            print "New batch: " + str(b)
        elif sys.argv[2] == "student":
            if len(sys.argv) <= 6:
                s = Student.create(
                    batch_id = sys.argv[3],
                    age = sys.argv[4],
                    last_name = sys.argv[5]
                )
                print "New Student: " + str(s)
            else:
                s = Student.create(
                    batch_id = sys.argv[3],
                    age = sys.argv[4],
                    last_name = sys.argv[5],
                    first_name = sys.argv[6]
                )
                print "New Student: " + str(s)
        elif sys.argv[2] == "exercise":
            e = Exercise.create(
                student_id = sys.argv[3],
                subject = sys.argv[4],
                note = sys.argv[5]
                )
            print "New exercise: " + str(e)

elif (sys.argv[1] == "delete"):
    if len(sys.argv) < 3:
        pass
    else:
        if sys.argv[2] == "school":
            school = School.get(School.id == sys.argv[3])
            School.delete_instance()
        elif sys.argv[2] == "batch":
            batch = Batch.get(Batch.id == sys.argv[3])
            batch.delete_instance()
        elif sys.argv[2] == "student":
            try:
                student = Student.get(Student.id == sys.argv[3])
                student.delete_instance()
                print "Delete:"
                print student
            except:
                print "Nothing to delete"
        elif sys.argv[2] == "exercice":
            print "hey"
            e = Exercise.get(Exercise.id == sys.argv[3])
            e.delete_instance()


elif (sys.argv[1] == "print_batch_by_school"):
    try:
        print Batch.get(school_id == sys.argv[2] )
    except:
        print "School not found"

elif (sys.argv[1] == "print_student_by_batch"):
    try:
        for student in Student.select().where(Student.batch == sys.argv[2]):
            print student
    except:
        print "Batch not found"

elif (sys.argv[1] == "print_student_by_school"):
    try:
        for student in Student.select().join(Batch).where(Batch.school_id == sys.argv[2]):
            print student
    except:
        print "School not found"

elif (sys.argv[1] == "print_family"):
    try:
        for student in Student:
            if (student.last_name == sys.argv[2]):
                print student
    except:
        print "Last name not found"

elif (sys.argv[1] == "age_average"):
    print Student.select(peewee.fn.Avg(Student.age)).scalar()

elif (sys.argv[1] == "change_batch"):
    if sys.argv[2] == student.id:
        print "%s already in %s" % (sys.argv[2], sys.argv[3])
    else:
        print "Student not found"

elif (sys.argv[1] == "print_all"):
    for S in School.select():
        print S
        for b in Batch.select().where(Batch.school == S.id):
            print "\t" + str(b)
            for s in Student.select().where(Student.batch_id == b.id):
                print "\t\t" + str(s)
                for e in Exercise.select().where(Exercise.student == s.id):
                    print "\t\t\t" + str(e)

elif (sys.argv[1] == "note_average_by_student"):
     note = Exercise.select().join(Student).where(Student.id == sys.argv[2])
     for n in note:
         print "%s: %s" % (n.subject, n.note)

elif (sys.argv[1] == "note_average_by_batch"):
    note = Exercise.select().join(Batch).where(Batch.id == sys.argv[2])
    for n in note:
        print "%s: %s" % (n.subject, n.note)

elif (sys.argv[1] == "note_average_by_school"):
    note = Exercise.select().join(School).where(School.id == sys.argv[2])
    for n in note:
        print "%s: %s" % (n.subjet, n.note)

    """if sys.argv[2] == str(school.id):
        student = Student.get(Student.id == sys.argv[3])
        print Student.select(peewee.fn.Avg(Student.note)).scalar()
    else:
        print "School not found"
"""

elif (sys.argv[1] == "top_batch"):
    if sys.arv[2] == batch.id:
        if sys.argv[3] == exercise.subject:
            print Student.oder_by(Student.note)
    else:
        print "Batch not found"

elif (sys.argv[1] == "top_school"):
      if sys.argv[2] == school.id:
          if sys.argv[3] == subject:
              print Student
      else:
          print "School not found"

elif (sys.argv[1] == "import_json"):
    school = School.select().get()

elif (sys.argv[1] == "export_json"):
    school = School.select().get()
    batch = Batch.select().get()
    student = Student.select().get()
    json_data = json.dumps(model_to_dict(school, batch, student))
    print json_data

else:
    print "Undefined action " % sys.argv[1]
