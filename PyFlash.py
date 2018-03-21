"""
PyFlash
Created by Bartosz Kosakowski
A small flash card program; fill a text file with questions
and answers in the form of question:answer and run the program.
"""
from pathlib import Path;
import os;

#checks for qa.txt and creates it in the program file's directory,
#otherwise confirms that the file was found
def CheckForFile():
	questionFile = Path("qa.txt");
	cwd = os.getcwd() #gets current working directory 
	if not questionFile.is_file():
		print("qa.txt not found, creating file in " + cwd);
		questionFile = open("qa.txt", "w");
		questionFile.close();
	else:
		print("qa.txt found");

#ADD CONDITION TO CHECK IF QUESTION ALREADY EXISTS
def AddQuestion():
	file = open("qa.txt", "a");
	q = input("enter a question:\n");
	a = input("enter the answer:\n");
	q += "\n";
	a += "\n";
	file.write(q);
	file.write(a);
	file.close();

def RemoveQuestion(question):
	qafile = open("qa.txt", "r+");
	qalist = qafile.read().splitlines();
	if question in qalist:
		answer = qalist[qalist.index(question)+1];
		splitFile = qafile.readlines();
		qafile.seek(0);
		for line in splitFile:
			if line is not question and line is not answer:
				qafile.write(line);
	else:
		print("question not found");
	qafile.close();

def ClearFile():
	os.remove("qa.txt");
	questionFile = open("qa.txt", "w");
	questionFile.close();

def ListQuestions():
	print("finish this");

def PrintWholeFile():
	qafile = open("qa.txt", "r+");
	qalist = qafile.read().splitlines();
	print(qalist);
	qafile.close();

def Run():
	CheckForFile();
	#AddQuestion();
	PrintWholeFile();
	RemoveQuestion(input("enter a question to remove:\n"));
	PrintWholeFile();

if __name__ == "__main__":
	Run();