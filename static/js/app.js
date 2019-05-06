// from data.js
var tableData = data;
console.log(tableData);

// References to HTML
const tbody = d3.select("tbody");
const dateField = d3.select("#datetime");
const filterButton = d3.select("#filter-btn")

// Array of columns for data
const columns = ["datetime", "city", "State", "country", "shape", "durationMinutes", "comments"];

// Function to populate the table
var populate = (input) => {
    input.forEach(sighting => {
      var row = tbody.append("tr");
      columns.forEach(column => row.append("td").text(sighting[column])
      )
    });
};

// Function to filter the data
filterButton.on("click", () => {
    d3.event.preventDefault();
    inputDate = dateField.property("value").trim();
    console.log(inputDate);
    var filterDate = tableData.filter(tableData => tableData.datetime === inputDate);

    // Clearing the old data from the table
    tbody.html("");

    // Clearing the dateField input
    dateField.node().value = "";

    // Running populate function with the filtered data if there is any data
    if (filterDate.length !== 0) {
        populate(filterDate);
        console.log(filterDate);
    }
    
    // Letting user know no results were found
    else {
        console.log("Sorry no results were found :(")
        window.alert("Sorry no results were found try 1/1/2010");
    };
});