Sub stock()

' Defining variables
Dim last_row As Double, volume as Double, count as Double, opening as Double, great_inc as double, great_dec as double, great_vol as double, tick_inc as string, tick_dec as string, tick_vol as string

' Looping through all the worksheets
For Each ws In Worksheets

    ' Setting initial values for variables
    volume = 0
    count = 2
    opening = ws.Range("C2").value

    ' Saving the number of rows
    last_row = ws.Cells(Rows.Count, 1).End(xlUp).Row

    ' Creating the new tables
    ws.Range("I1").value = "Ticker"
    ws.Range("J1").value = "Yearly Change"
    ws.Range("K1").value = "Percent Change"
    ws.Range("L1").value = "Total Stock Volume"
    ws.Range("P1").value = "Ticker"
    ws.Range("Q1").value = "Value"
    ws.Range("O2").value = "Greatest % Increase"
    ws.Range("O3").value = "Greatest % Decrease"
    ws.Range("O4").value = "Greatest Total Volume"

    ' Looping through all the rows
    for i = 2 to last_row

        ' Summing all the volumes
        volume = volume + ws.Cells(i,7).value        

        ' Checking if the next ticker is different than the current ticker
        if ws.Cells(i,1).value <> ws.Cells(i+1,1).value then

            ' Recording all the desired values in the new table
            ws.Cells(count,9).value = ws.Cells(i,1).value
            ws.Cells(count,12).value = volume
            ws.Cells(count,10).value = (ws.Cells(i,6).value - opening)

            ' Calculating the Percent Change
            if opening = 0 then
                ' Stupid PLNT
                ws.Cells(count,11).value = 0
            else
                ws.Cells(count,11).value = (ws.cells(count,10).value / opening)
            end if

            ' Recording the new opening value
            opening = ws.cells(i+1,3).value

            ' Incrementing count for the next row and resetting volume to 0
            count = count + 1
            volume = 0
        end if
    next i

    ' Recording the initial values from the new table
    tick_inc = ws.Range("I2").value
    tick_dec = ws.Range("I2").value
    tick_vol = ws.Range("I2").value
    great_inc = ws.Range("K2").value
    great_dec = ws.Range("K2").value
    great_vol = ws.Range("L2").value

    ' Looping through the new table
    for j = 2 to count

        ' Displaying the percent change as an actual percent duhhhhhh
        ws.cells(j,11).numberformat = "0.00%"

        ' Formatting the yearly change cell to be green if +ve, red if -ve and white if 0
        if ws.cells(j,10).value > 0 then
            ws.cells(j,10).interior.colorindex = 4

        elseif ws.cells(j,10).value < 0 then
            ws.cells(j,10).interior.colorindex = 3
        end if

        ' Finding the greatest % increase
        if ws.cells(j,11).value > great_inc then
            great_inc = ws.cells(j,11).value
            tick_inc = ws.cells(j,9).value
        end if

        ' Finding the greatest % dec
        if ws.cells(j,11).value < great_dec then
            great_dec = ws.cells(j,11).value
            tick_dec = ws.cells(j,9).value
        end if        

        ' Finding the greatest volume
        if ws.cells(j,12).value > great_vol then
            great_vol = ws.cells(j,12).value
            tick_vol = ws.cells(j,9).value
        end if 
    next j

    ' Recording the values of the greatest in the new new table
    ' Maybe do this in an array and loop next time?
    ws.Range("P2").value = tick_inc
    ws.Range("Q2").value = great_inc
    ws.Range("P3").value = tick_dec
    ws.Range("Q3").value = great_dec
    ws.Range("P4").value = tick_vol
    ws.Range("Q4").value = great_vol
Next ws
End Sub