# GPo, 2021 

# 'Apply filters' applies filters to a frame area selected in the timeline.
# First create selections in the timeline with the Trim Editor and click with the right mouse button 
# on a selected area and select 'Apply filter' and the desired filter.

###### Parameters for the templates ################
#  %start is replaced with selection start         #
#  %stop is replaced with selection end            #
#  %* is replaced with the script selected text    #
#  %join joins the filters from each selected line #
#  %copy copies the selection to script end        #
#  %> copies this line to all timeline selections  #
####################################################

## Simple filter example ( You have to put the text cursor at the desired script insert position ): 
ApplyRange(%start, %stop, "sharpen", 0.4) or c1=Trim(%start, %stop).sharpen(0.4)

## Example with a single line (filter) selection in the script:
# if a single line is selected, disabled filters # are enabled 
ApplyFilter(%start, %stop, """%*""")

## With a single line (filter) selection, but does not override the selection (filter is inserted at script end)
ApplyFilter(%start, %stop, """%*%copy""")

## Below you can see an example with several lines (filters) selected in the script, disabled lines # are ignored 
# and comments after filter text e.g. sharpen(0.4) # my sharpener, are removed. 

## Method: add preview filter, insert script selections, join the filters and apply the filters from start to stop  
# This two examples are included as default in the templates, when you have saved the function 'ApplyFilter' listed below, 
# you can run the template in the timeline selections popup menu. You can also change it, e.g. remove 'avsp_filter'
# Script selections are always replaced with the result, but there is the parameter %copy if you use this parameter 
# the selected text (filters) are copied to the script end. 

## for a single timeline selection
filter = """\
%*%join
\"""
ApplyFilter(%start, %stop, filter)

## for all timeline selections
filter = """\
%*%join
\"""
%>ApplyFilter(%start, %stop, filter) # %> this text is added for all selections 

## Manual multiple filter example (you can save it as template, Options > 'Apply filters...'): 
filter = """\
SmoothLevels(input_low=16, gamma=1.00, input_high=235, output_low=16, output_high=235, TVrange=True, Lmode=0, darkSTR=100, brightSTR=100, debug=False)
\.SmoothTweak(brightness=0, contrast=1.00, saturation=1.00, hue1=0, hue2=0, TVrange=True, Lmode=0, limitSTR=100, debug=False)
\.NonlinUSM(z=1.0, pow=1.2, str=0.25, rad=120)
\.NonlinUSM(z=3, pow=1.2, str=0.22, rad=6)
\"""
ApplyFilter(%start, %stop, filter)
# or %>ApplyFilter(%start, %stop, filter) for all selections


## ApplyFilter syntax, save it separate in your filters avsi file or as ApplyFilter.avsi 
# If you have a better alternative to the function ApplyFilter or a better procedure, please let me know.

function ApplyFilter(clip c, int "start", int "end", string "filter"){
    start = default(start, 0)
    end = default(end, 0)
    c
    end = end <= 0 ? FrameCount()-1 : end
    seg2 = Trim(start, end)
    seg2 = Eval("seg2." + filter) 
    re = start == 0 ? seg2 : start == 1 ? Trim(0, -1) ++ seg2 : Trim(0, start-1) ++ seg2
    re = end < FrameCount-1 ? re ++ Trim(end + 1, 0) : re
    return re
}

