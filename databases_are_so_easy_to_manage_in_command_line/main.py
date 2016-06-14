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
            for S in School.select():
                print S
        elif sys.argv[2] == "batch":
            for b in Batch.select():
                print b
        elif sys.argv[2] == "user":
            for u in Users.select():
                print u
        elif sys.argv[2] == "student":
            for s in Student.select():
                print s
        elif sys.argv[2] == "exercise":
            for e in Exercise.select():
                print e

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
        elif sys.argv[2] == "exercise":
            exercise = Exercise.get(Exercise.id == sys.argv[3])
            exercise.delete_instance()


elif (sys.argv[1] == "print_batch_by_school"):
    try:
        batch = Batch.get(id == sys.argv[2])
        print batch
    except:
        print "School not found"

elif (sys.argv[1] == "print_student_by_batch"):
    try:
        for s in Student.select().where(Student.batch == sys.argv[2]):
		          print s
    except:
        print "Batch not found"

elif (sys.argv[1] == "print_student_by_school"):
     try:
        for b in Batch.select().where(Batch.school == sys.argv[2]):
		          for s in Student.select().where(Student.batch == b):
			                   print s
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
    avg = Student.select(peewee.fn.Avg(Student.age)).scalar()
    print "%d" % (avg)
elif (sys.argv[1] == "change_batch"):
    student = Student.get(Student.id == sys.argv[2])
    batch = Batch.get(Batch.id == sys.argv[3])
    if student.batch == batch:
        print "%s already in %s" % (student, batch)
    else:
        print "%s has been moved to %s" % (student, batch)
        student.batch = sys.argv[3]
        student.save()

elif (sys.argv[1] == "print_all"):
    for S in School.select():
        print S
        for b in Batch.select().where(Batch.school == S):
            print "\t" + str(b)
            for s in Student.select().where(Student.batch_id == b):
                print "\t\t" + str(s)
                for e in Exercise.select().where(Exercise.student == s):
                    print "\t\t\t" + str(e)

elif (sys.argv[1] == "note_average_by_student"):
    if len(sys.argv) <= 2:
        pass
    try:
        student = Student.get(Student.id == sys.argv[2])
    except:
        print "Student not found"
        pass
    grades = Exercise.select().where(Exercise.student == sys.argv[2]).group_by(Exercise.subject)
    for n in grades:
        avg = Exercise.select(peewee.fn.Avg(Exercise.note)).where(Exercise.student == sys.argv[2], Exercise.subject == n.subject).scalar()
        print "%s: %g" % (n.subject,avg)

elif (sys.argv[1] == "note_average_by_batch"):
    if len(sys.argv) <= 2:
        pass
    try:
        batch = Batch.get(Batch.id == sys.argv[2])
    except:
        print "Batch not found"
        pass
    grades = Exercise.select(Exercise.subject).join(Student).where(Student.batch == sys.argv[2]).group_by(Exercise.subject)
    for n in grades:
        avg = n.select(peewee.fn.Avg(Exercise.note)).join(Student, on=Exercise.student).where(Student.batch == sys.argv[2], Exercise.subject == n.subject).scalar()
        print "%s: %g" % (n.subject, avg)

elif (sys.argv[1] == "note_average_by_school"):
    if len(sys.argv) <= 2:
        pass
    try:
        school = School.get(School.id == sys.argv[2])
    except:
        print "School not found"
        pass
    grades = Exercise.select(Exercise.subject).join(Student, on=Exercise.student).join(Batch, on=Student.batch).where(Batch.school == sys.argv[2]).group_by(Exercise.subject)
    for n in grades:
        avg = n.select(peewee.fn.Avg(Exercise.note)).where(Exercise.subject == n.subject).scalar()
        print "%s: %g" % (n.subject, avg)

elif (sys.argv[1] == "top_batch"):
     if len(sys.argv) == 3:
         try:
             school = School.get(School.id == sys.argv[2])
             student =Student.select(Student).join(Batch, on=Student.batch).join(Exercise, on=Exercise.student).where(Batch.school == school).group_by(Batch.school).having(Exercise.note == peewee.fn.MAX(Exercise.note))
             for s in student:
                 print "%s" % (s)
         except:
             print "School not found"
     elif len(sys.argv) == 4:
         try:
             batch = Batch.get(Batch.id == sys.argv[2])
             student = Student.select(Student).join(Exercise, on=Exercise.student).where(Student.batch == batch, Exercise.subject == sys.argv[3]).group_by(Student.batch).having(Exercise.note == peewee.fn.MAX(Exercise.note))
             for s in student:
                 print "%s" % (s)
         except:
             print "Batch not found"
             pass

elif (sys.argv[1] == "top_school"):
    if len(sys.argv) == 3:
        try:
            school = School.get(School.id == sys.argv[2])
            student = Student.select(Student).join(Batch, on=Student.batch).join(Exercise, on=Exercise.student).where(Batch.school == school).group_by(Batch.school).having(Exercise.note == peewee.fn.MAX(Exercise.note))
            for s in student:
                print "%s" % (s)
        except:
            print "School not found"
    elif len(sys.argv) == 4:
        try:
            school = School.get(School.id == sys.argv[2])
            students =Student.select(Student).join(Batch, on=Student.batch).join(Exercise, on=Exercise.student).where(Batch.school == school, Exercise.subject == sys.argv[3]).group_by(Batch.school).having(Exercise.note == peewee.fn.MAX(Exercise.note))
            for s in students:
                print "%s" % (s)
        except:
            print "School not found"
            pass

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
