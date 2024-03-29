export function scatter(data, statX, statY) {
  //const statX = 'k';
  //const statY = 'hr';

  // set the dimensions and margins of the graph
  var margin = { top: 10, right: 30, bottom: 30, left: 60 },
    width = 1000 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  d3.select('#my_dataviz').html('')
  var svg = d3.select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");


  // Add X axis
  var x = d3.scaleLinear()
    .domain(d3.extent(data, d => d[statX])).nice()
    .range([0, width]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    //.domain([0, 80])
    .domain(d3.extent(data, d => d[statY])).nice()
    .range([height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
  // Its opacity is set to 0: we don't see it by default.
  var tooltip = d3.select("#my_dataviz")
    .append("div")
    .style("opacity", 0)
    .attr("class", "tooltip")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "1px")
    .style("border-radius", "5px")
    .style("padding", "10px")

  // A function that change this tooltip when the user hover a point.
  // Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
  var mouseover = function (d) {
    tooltip
      .style("opacity", 1)

    dot.style("fill", (z) => (d.player == z.player) ? "orange" : "#69b3a2");
  }

  const formatLabel = (d) => {
    const {player, year, ...rest} = d

    const stats = Object.entries(rest).map(([k,v]) => `${k}=${v}`).join(' ')

    return `${player} ${year} | ${stats}`

  }

  var mousemove = function (d) {
    tooltip
      .html(formatLabel(d))
      .style("left", (d3.mouse(this)[0] + 90) + "px") // It is important to put the +90: other wise the tooltip is exactly where the point is an it creates a weird effect
      .style("top", (d3.mouse(this)[1]) + "px")
  }

  // A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
  var mouseleave = function (d) {
    tooltip
      .transition()
      .duration(200)
      .style("opacity", 0)
    dot.style("fill", "#69b3a2");
  }

  // Add dots
  var dot = svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", function (d) { return x(d[statX]); })
    .attr("cy", function (d) { return y(d[statY]); })
    .attr("r", 4)
    .style("fill", "#69b3a2")
    .style("opacity", 1)
    .style("stroke", "white")
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
}

//import data from './k-hr-yr.json'
//console.log(data)
//scatter(data, '#my_dataviz')