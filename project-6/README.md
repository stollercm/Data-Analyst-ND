##SUMMARY

The data visualization shows the differences in how the US job market changed
between 2007 and 2013 for Millennials versus for Baby Boomers. We can see that
Baby Boomers enjoyed job growth in most categories, while Millennials suffered
from declines in many categories. It is interesting to note the categories that
had big disparities in growth trends between these two generational groups.

________________________________________________________________________________

##DESIGN

I decided to use bar graphs for this visualization because the occupation
types are categorical data that makes for good bins for the bars, and the job
change values are numerical and read well as position/length elements of the
visualization. Using color to denote generation made sense because it shows the
difference between those two categories quickly.

At first, I tried a stacked, paired bar graph to show change over time (in the
pairings 2007/2013) as well as composition of the category in terms of
generation (Baby Boomer/Millennial). This proved to be problematic and did not
show the data story clearly at all. I pared down the visualization by taking
the rate of job growth as the positional variable and switching the pairing
of the bars to the generation categories. This was close, but lacked the scale
of each category, so you had no sense of what those job growth numbers meant in
the greater market. Finally, I used raw job change values, maintaining the rate
information in the tooltips. This combination of length and direction make the
discrepancies in job change between groups very clear. It shows the magnitude
of any change as well as gives context to the size of the category through the
combination of the visual cue of length and the growth rate in the tooltip.

________________________________________________________________________________

##FEEDBACK

###Version 1 - index1.html - Person A

What do you notice in the visualization?

    It looks like there are more Millennials than Baby Boomers in many of the
    categories, but this display makes it hard to tell. Also, a major problem
    is that in each pair of bars (as in, for each job category) the order of
    years is inconsistent. Sometimes 2007 is first, sometimes 2013 is first.
    That makes it impossible to see the change that you're trying to show.

What questions do you have about the data?

    What are the changes really like during this time period? How big of a
    change is it in each generation group?

What relationships do you notice?

    For each job category, there does not seem to be much change between the
    two years overall. Growth or decline in each group is too hard to see.

What do you think is the main takeaway from this visualization?

    There were more Millennials than Baby Boomers in the workforce during this
    time period.

Is there something you don’t understand in the graphic?

    If the above takeaway is what we're supposed to glean from this, there is
    probably a better way to show that. This graphic doesn't seem to tell the
    story about differences in change that you're trying to tell.

\\\\\\\\\\\\\\\\\\\\\\\\\

** Switched from a stacked, paired bar graph with raw job numbers to a paired
bar graph showing rates of change.

###Version 2 - index2.html - Person A (again)

What do you notice now?

    This graphic says a lot more about how job numbers changed during the time
    period in question. It gives the reader a sense of the disparities in job
    growth between the groups. You can really see that Baby Boomers saw job
    growth in all occupations but one, and that Millennials had slower growth
    and even decline in almost all occupations.

###Version 2 - index2.html - Person B

What do you notice in the visualization?

    The baby boomers were much more able to increase their number of jobs than
    millennials.

What questions do you have about the data?

    Why is it in decimal and not percent? Changing the axis labels to percents
    would be clearer - right now I'm not sure if 0.05 is 0.05% or 5% because I
    think of job growth as percentages.
    What age range is being considered for baby boomers and millennials?
    Different groups define this differently.

What relationships do you notice?

    Baby Boomers are much less likely to have decreased job numbers and more
    likely to have increased job numbers.

What do you think is the main takeaway from this visualization?

    Baby boomers, even though aging, still are moving to new jobs, and coming
    back from retirement or from being laid off in the recession.

Is there something you don’t understand in the graphic?

    It would be better to have a clearer title that explains the data set a bit
    better.

###Version 2 - index2.html - Person C

What do you notice in the visualization?

    The tooltip is nice because it gives the rate value and generation & job
    info.

What questions do you have about the data?

    How big are these changes in terms of raw numbers? How big are the
    categories in general? I like the story you're telling with the growth
    rates, but a high growth rate could just be a result of a small category
    getting a moderate increase in jobs. That information would add to the
    story.

What relationships do you notice?

    The biggest differences in job growth were in occupations in Production;
    Architecture and Engineering; Installation, Maintenance, and Repair;
    Transportation and Material Moving; Office and Admin Support; Business and
    Financial Ops; and Computer and Math.

What do you think is the main takeaway from this visualization?

    Baby boomers stayed in the job market and even added jobs during this time,
    contributing to fewer jobs being available for millennials.

Is there something you don’t understand in the graphic?

    no

\\\\\\\\\\\\\\\\\\\\\\\\\

** Switched to Job Change numbers instead of Rates; enhanced tooltip

###Version 3 - index3.html - Person B (again)

What do you notice now?

    The changes are less normalized now with the raw numbers rather than rates,
    but I kind of like it. This shows the market more holistically. But your
    colors got mixed up, clearly Millennials should be salmon.

###Version 3 - index3.html - Person C (again)

What do you notice now?

    I like the move to actual change numbers. Disparities that seemed so big
    in Arch and Engineering; Installation, Maintenance, and Repair;
    Transportation and Material Moving; Business and Financial Ops; and
    Computer and Math are put into the perspective of size of the category,
    while the disparities in Food Preparation/Serving, Office and Admin, and
    Construction are very obvious indicators of difference in the job market
    besides just growth/change. I also like that you kept the rates by putting
    them in the tooltips.

###Version 3 - index3.html - Person D

What do you notice in the visualization?

    I notice that there are some occupations for which there is a big disparity
    between the two generational groups in terms of growth or decline in that
    job category.

What questions do you have about the data?

    What kinds of jobs make up these categories?

What relationships do you notice?

    The occupation with the best growth for Boomers saw the worst decline for
    Millennials (Office & Admin Support). All of the categories except for one
    that show a decline in jobs held by Millennials show at least some growth
    among Boomers. The occupations that saw the most growth among Millennials
    were also fairly strong among Boomers. Some occupations were pretty stagnant
    for both groups.

What do you think is the main takeaway from this visualization?

    The job market is tougher for Millennials than for Baby Boomers.

Is there something you don’t understand in the graphic?

    No.
    
________________________________________________________________________________

##RESOURCES

Sample Data Sets - Tableau Public. <https://public.tableau.com/s/resources>

Dimple Examples. <http://dimplejs.org/examples_index.html>

Dimple Documentation. <https://github.com/PMSI-AlignAlytics/dimple/wiki>
