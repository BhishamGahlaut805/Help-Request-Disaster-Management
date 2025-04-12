//Just-Example Code
// This code demonstrates how to use PythonShell to run a Python script from Node.js
const { PythonShell } = require("python-shell");

let inputData = {
  Lon: 80.2707,
  Lat: 13.0827,
  Pin: 600001,
  Location: "Urban",
  Des: "Building collapse in residential area due to earthquake, people trapped under rubble",
  PeopleCount: 40,
};

// Options for PythonShell
let options = {
  mode: "json",
  pythonOptions: ["-u"],
  scriptPath: "./", // path to your Python script
  args: [JSON.stringify(inputData)],
};

PythonShell.run("predict_priority.py", options, (err, results) => {
  if (err) throw err;
  console.log("Predicted Priority:", results[0]);
});
