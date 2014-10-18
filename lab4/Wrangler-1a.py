from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split data repeatedly on newline  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\n",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Extract from data on 'CMSC any number '
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="CMSC\\d+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Fill extract  with values from above
w.add(dw.Fill(column=["extract"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Wrap  rows where data starts with '0'
w.add(dw.Wrap(column=[],
              table=0,
              status="active",
              drop=False,
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.StartsWith(column=[],
                    table=0,
                    status="active",
                    drop=False,
                    lcol="data",
                    value="0",
                    op_str="starts with")])))

# Delete row 1
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowIndex(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  indices=[0])])))

# Drop wrap3, wrap5, wrap9, wrap7
w.add(dw.Drop(column=["wrap3","wrap5","wrap9","wrap7"],
              table=0,
              status="active",
              drop=True))

# Drop wrap10, wrap11, wrap12, wrap13
w.add(dw.Drop(column=["wrap10","wrap11","wrap12","wrap13"],
              table=0,
              status="active",
              drop=True))

# Set  wrap1  name to  Course No.
w.add(dw.SetName(column=["wrap1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Course No."],
                 header_row=None))

# Set  wrap  name to  Section No.
w.add(dw.SetName(column=["wrap"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Section No."],
                 header_row=None))

# Set  Section_No.  name to  Section No
w.add(dw.SetName(column=["Section_No."],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Section No"],
                 header_row=None))

# Set  Section_No  name to  Section No
w.add(dw.SetName(column=["Section_No"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Section No"],
                 header_row=None))

# Set  Section_No1  name to  Section No
w.add(dw.SetName(column=["Section_No1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Section No"],
                 header_row=None))

# Set  Course_No.  name to  Course_No
w.add(dw.SetName(column=["Course_No."],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Course_No"],
                 header_row=None))

# Extract from wrap8 after '  '
w.add(dw.Extract(column=["wrap8"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=None,
                 after="  ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from wrap8 on ' any word '
w.add(dw.Extract(column=["wrap8"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="[a-zA-Z]+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop wrap8
w.add(dw.Drop(column=["wrap8"],
              table=0,
              status="active",
              drop=True))

# Extract from wrap6 after ' any word  '
w.add(dw.Extract(column=["wrap6"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=None,
                 after="[a-zA-Z]+ ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from wrap6 on ' any word '
w.add(dw.Extract(column=["wrap6"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="[a-zA-Z]+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop wrap6
w.add(dw.Drop(column=["wrap6"],
              table=0,
              status="active",
              drop=True))

# Extract from wrap4 between ' Waitlist: ' and ')'
w.add(dw.Extract(column=["wrap4"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before="\\)",
                 after=" Waitlist: ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from wrap4 between 'Open: ' and ','
w.add(dw.Extract(column=["wrap4"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=",",
                 after="Open: ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from wrap4 between ': ' and ','
w.add(dw.Extract(column=["wrap4"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=",",
                 after=": ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop wrap4
w.add(dw.Drop(column=["wrap4"],
              table=0,
              status="active",
              drop=True))

# Set  wrap2  name to  Instructor
w.add(dw.SetName(column=["wrap2"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Instructor"],
                 header_row=None))

# Set  extract6  name to  Seats
w.add(dw.SetName(column=["extract6"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Seats"],
                 header_row=None))

# Set  extract5  name to  Open
w.add(dw.SetName(column=["extract5"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Open"],
                 header_row=None))

# Set  extract4  name to  Wait List
w.add(dw.SetName(column=["extract4"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Wait List"],
                 header_row=None))

# Set  extract3  name to  Days
w.add(dw.SetName(column=["extract3"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Days"],
                 header_row=None))

# Set  extract2  name to  Times
w.add(dw.SetName(column=["extract2"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Times"],
                 header_row=None))

# Set  Times  name to  Time
w.add(dw.SetName(column=["Times"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Time"],
                 header_row=None))

# Set  extract1  name to  Building
w.add(dw.SetName(column=["extract1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Building"],
                 header_row=None))

# Set  Building  name to  Bldg.
w.add(dw.SetName(column=["Building"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Bldg."],
                 header_row=None))

# Set  extract  name to  Room No
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Room No"],
                 header_row=None))

# Merge Course_No, Section_No  with glue  ,
w.add(dw.Merge(column=["Course_No","Section_No"],
               table=0,
               status="active",
               drop=False,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               glue=","))

# Extract from merge after ','
w.add(dw.Extract(column=["merge"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=None,
                 after=",",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from merge on 'CMSC any number '
w.add(dw.Extract(column=["merge"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="CMSC\\d+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop Section_No, merge, Course_No
w.add(dw.Drop(column=["Section_No","merge","Course_No"],
              table=0,
              status="active",
              drop=True))

# Set  extract7  name to  Course No
w.add(dw.SetName(column=["extract7"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Course No"],
                 header_row=None))

# Set  extract  name to  Section No
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Section No"],
                 header_row=None))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])
