import MDAnalysis
import MDAnalysis.analysis.contacts
from MDAnalysis.tests.datafiles import PSF,DCD

# example trajectory (transition of AdK from closed to open)
u = MDAnalysis.Universe(PSF,DCD)

# crude definition of salt bridges as contacts between NH/NZ in ARG/LYS and OE*/OD* in ASP/GLU.
# You might want to think a little bit harder about the problem before using this for real work.
sel_basic = "(resname ARG or resname LYS) and (name NH* or name NZ)"
sel_acidic = "(resname ASP or resname GLU) and (name OE* or name OD*)"

# reference groups (first frame of the trajectory, but you could also use a separate PDB, eg crystal structure)
acidic = u.selectAtoms(sel_acidic)
basic = u.selectAtoms(sel_basic)

# set up analysis of native contacts ("salt bridges"); salt bridges have a distance <6 A
CA1 = MDAnalysis.analysis.contacts.ContactAnalysis1(u, selection=(sel_acidic, sel_basic), refgroup=(acidic, basic), radius=6.0, outfile="qsalt.dat")

# iterate through trajectory and perform analysis of "native contacts" q
# (force=True ignores any previous results, force=True is useful when testing)
CA1.run(force=True)

# plot time series q(t) [possibly do "import pylab; pylab.clf()" do clear the figure first...]
CA1.plot(filename="adk_saltbridge_contact_analysis1.pdf", linewidth=3, color="blue")

# or plot the data in qsalt.dat yourself.
CA1.plot_qavg(filename="adk_saltbridge_contact_analysis1_matrix.pdf")