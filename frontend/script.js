document.addEventListener("DOMContentLoaded", async () => {
    const searchBox = document.getElementById("search-box");
    const dataTableBody = document.querySelector("#data-table tbody");

    // Function to fetch data from the backend
    async function fetchData(query = "") {
        const response = await fetch(`/search?q=${query}`);
        const data = await response.json();
        return data;
    }

    // Function to populate the table
    function populateTable(data) {
        dataTableBody.innerHTML = ""; // Clear existing rows

        if (data.length === 0) {
            const row = document.createElement("tr");
            const cell = document.createElement("td");
            cell.colSpan = 8;
            cell.textContent = "No results found";
            row.appendChild(cell);
            dataTableBody.appendChild(row);
        } else {
            data.forEach((item) => {
                const row = document.createElement("tr");
                Object.values(item).forEach((value) => {
                    const cell = document.createElement("td");
                    cell.textContent = value;
                    row.appendChild(cell);
                });
                dataTableBody.appendChild(row);
            });
        }
    }

    // Fetch and display all data initially
    const allData = await fetchData();
    populateTable(allData);

    // Add event listener to search box for dynamic filtering
    searchBox.addEventListener("input", async (event) => {
        const query = event.target.value;
        const filteredData = await fetchData(query);
        populateTable(filteredData);
    });
});
