#Import The PSCAD Automation Library:
import mhrc.automation

#Launch PSCAD
#pscad= mhrc.automation.launch_pscad(certificate=False)

#Check The PSCAD Installations We Have:
controller = mhrc.automation.controller()
pscad_versions = controller.get_paramlist_names('pscad')
print(pscad_versions)

#Check The Fortran Installations We Have:
fortran_versions = controller.get_paramlist_names('fortran')
print(fortran_versions)

#Launching PSCAD
pscad=mhrc.automation.launch_pscad(fortran_version=fortran_versions[2],pscad_version=pscad_versions[1],certificate=False, minimize=True)

#Check Setting Of Launched PSCAD
#Print The Setting of Launched PSCAD
for key, value in (pscad.settings().items()):
    print("%s: %s" % (key, value))

#Load A Project Or A Workspace
pscad.load(r'C:\Users\Public\Documents\PSCAD\4.6\Examples\Protection\protection_x4.pscx')

#Run The Project
exCase = pscad.project('protection_x4')
exCase.run()

#Print Output Messages
print(exCase.get_output_text())















