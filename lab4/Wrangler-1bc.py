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

# Split data repeatedly on '|'
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="\\|",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character="\""))

# Cut  on '"'
w.add(dw.Cut(column=[],
             table=0,
             status="active",
             drop=False,
             result="column",
             update=True,
             insert_position="right",
             row=None,
             on="\"",
             before=None,
             after=None,
             ignore_between=None,
             which=1,
             max=0,
             positions=None))

# Drop split
w.add(dw.Drop(column=["split"],
              table=0,
              status="active",
              drop=True))

# Extract from split1 between '[\[' and ' FIFA'
w.add(dw.Extract(column=["split1"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" FIFA",
                 after="\\[\\[",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop split1
w.add(dw.Drop(column=["split1"],
              table=0,
              status="active",
              drop=True))

# Extract from split2 between '[\[' and ' FIFA'
w.add(dw.Extract(column=["split2"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" FIFA",
                 after="\\[\\[",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop split2
w.add(dw.Drop(column=["split2"],
              table=0,
              status="active",
              drop=True))

# Extract from split3 before '}}'
w.add(dw.Extract(column=["split3"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before="}}",
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from split3 between '[\[' and ' FIFA'
w.add(dw.Extract(column=["split3"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" FIFA",
                 after="\\[\\[",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop split3
w.add(dw.Drop(column=["split3"],
              table=0,
              status="active",
              drop=True))

# Extract from split4 between '[\[' and ' FIFA'
w.add(dw.Extract(column=["split4"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" FIFA",
                 after="\\[\\[",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop split4
w.add(dw.Drop(column=["split4"],
              table=0,
              status="active",
              drop=True))

# Extract from split5 between '[\[' and ' FIFA'
w.add(dw.Extract(column=["split5"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" FIFA",
                 after="\\[\\[",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop split5
w.add(dw.Drop(column=["split5"],
              table=0,
              status="active",
              drop=True))

# Extract from split6 between '[\[' and ' FIFA'
w.add(dw.Extract(column=["split6"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" FIFA",
                 after="\\[\\[",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop split6
w.add(dw.Drop(column=["split6"],
              table=0,
              status="active",
              drop=True))

# Drop split7
w.add(dw.Drop(column=["split7"],
              table=0,
              status="active",
              drop=True))

# Fill extract2  with values from above
w.add(dw.Fill(column=["extract2"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete empty rows
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Empty(column=[],
               table=0,
               status="active",
               drop=False,
               percent_valid=0,
               num_valid=0)])))

# Merge extract2, extract, extract1, extract3...  with glue  ,
w.add(dw.Merge(column=["extract2","extract","extract1","extract3","extract4","extract5","extract6"],
               table=0,
               status="active",
               drop=False,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               glue=","))

# Drop extract, extract1, extract3, extract2...
w.add(dw.Drop(column=["extract","extract1","extract3","extract2","extract4","extract5","extract6"],
              table=0,
              status="active",
              drop=True))

# Split merge repeatedly on ','
w.add(dw.Split(column=["merge"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on=",",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Delete  rows where split8 is null
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="split8",
                value=None,
                op_str="is null")])))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])
