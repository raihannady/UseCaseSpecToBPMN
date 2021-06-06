from django.shortcuts import render,redirect
from app.models import projectlist, scenariolist
from app.forms import projectform, scenarioform
import xml.etree.ElementTree as ET
# Create your views here.

def index(request):
	resultsdisplay=projectlist.objects.all()
	return render(request,'project_list.html',{'resultsdisplay':resultsdisplay})

def createproject(request):
    form=projectform()
    if request.method == 'POST':
       form=projectform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/project_list')
    context = {'form':form}
    return render (request, 'project_list_form.html',context)

def updateproject(request,pk):
    projectupdate=projectlist.objects.get(no=pk)
    form=projectform(instance=projectupdate)
    if request.method == 'POST':
       form=projectform(request.POST,instance=projectupdate)
       if form.is_valid():
           form.save()
           return redirect('/project_list')
    context = {'form':form}
    return render (request, 'project_list_form.html',context)


def indexscenario(request,no):
	scenariodisplay=scenariolist.objects.filter(projectno_id=no)
	return render(request,'scenario_list.html',{'scenariodisplay':scenariodisplay})

def createscenario(request):
    form=scenarioform()
    if request.method == 'POST':
       form=scenarioform(request.POST)
       if form.is_valid():
           form.save()
           scenarioupdate=scenariolist.objects.latest('no')
           return redirect('index', no=scenarioupdate.projectno_id)
    context = {'form':form}
    return render (request, 'scenario_list_form.html',context)

def updatescenario(request,pk):
    scenarioupdate=scenariolist.objects.get(no=pk)
    form=scenarioform(instance=scenarioupdate)
    if request.method == 'POST':
       form=scenarioform(request.POST,instance=scenarioupdate)
       if form.is_valid():
           form.save()
           return redirect('index', no=scenarioupdate.projectno_id)
    context = {'form':form}
    return render (request, 'scenario_list_form.html',context)

def deletescenario(request,pk):
    scenariodel=scenariolist.objects.get(no=pk)
    hantu = scenariolist.objects.filter(no=pk).values_list('projectno_id', flat=True).first()
    scenariodel.delete()
    return redirect('index', no=scenariodel.projectno_id)

def Generate(request):
    resultsdisplay=scenariolist.objects.all
    for x in resultsdisplay():
        y = str(x.scenarioid)
        panjangx= str(x.scenarioid*150)
        if x.scenarioid == 1:
            filexml = ".\staticfiles\mediafiles\sbpmnawal.bpmn"
            tree = ET.parse(filexml)
            root = tree.getroot()
            action = root.find(".//process")
            doc = ET.SubElement(action, "task")
            doc.set('id','acsajja'+y)
            doc.set('name',x.scenario)
            act = root.find(".//task")
            b = ET.SubElement(act, 'Description')
            act1 = root.find(".//{http://www.omg.org/spec/BPMN/20100524/DI}BPMNPlane")
            doc1 = ET.SubElement(act1, "{http://www.omg.org/spec/BPMN/20100524/DI}BPMNShape")
            doc1.set('id','acsajja'+y+'_di')
            IDSHAPE= 'acsajja'+y+'_di'
            print(IDSHAPE)
            doc1.set("bpmnElement",'acsajja'+y)
            act1 = root.find('.//{http://www.omg.org/spec/BPMN/20100524/DI}BPMNShape/[@id="%s"]' %IDSHAPE)
            print(act1)
            c = ET.SubElement(act1, '{http://www.omg.org/spec/DD/20100524/DC}Bounds')
            c.set('x',panjangx)
            c.set('y','100')
            c.set('width','57')
            c.set('height','40')
            tree.write(".\staticfiles\mediafiles\hasil7.bpmn")
        else:
            filexml = ".\staticfiles\mediafiles\hasil7.bpmn"
            tree = ET.parse(filexml)
            root = tree.getroot()
            print(root)
            action = root.find(".//process")
            print(action)
            doc = ET.SubElement(action, "task")
            doc.set('id', 'acsajja'+y)
            idtask = 'acsajja'+y
            print(idtask)
            doc.set('name',x.scenario)
            act = root.find('.//task[@id="%s"]' %idtask)
            b = ET.SubElement(act, 'Description')
            act1 = root.find(".//{http://www.omg.org/spec/BPMN/20100524/DI}BPMNPlane")
            doc1 = ET.SubElement(act1, "{http://www.omg.org/spec/BPMN/20100524/DI}BPMNShape")
            doc1.set('id', 'acsajja'+y+'_di')
            idShape = 'acsajja'+y+'_di'
            doc1.set("bpmnElement", 'acsajja'+y)
            act1 = root.find('.//{http://www.omg.org/spec/BPMN/20100524/DI}BPMNShape/[@id="%s"]' %idShape)
            c = ET.SubElement(act1, '{http://www.omg.org/spec/DD/20100524/DC}Bounds')
            c.set('x', panjangx)
            c.set('y', '100')
            c.set('width', '57')
            c.set('height', '40')
            tree.write(".\staticfiles\mediafiles\hasil7.bpmn")
    filexml = ".\staticfiles\mediafiles\hasil7.bpmn"
    tree = ET.parse(filexml)
    root = tree.getroot()
    root.set('xmlns',"http://www.omg.org/spec/BPMN/20100524/MODEL")
    tree.write(".\staticfiles\mediafiles\hasil7.bpmn")
    return render(request, 'coba.html')