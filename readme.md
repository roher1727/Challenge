# Code Challenge

Create a web service using any framework that flattens a nested sequence into a single list of values.

### Input


```javascript
{
	"items":[1, 2, [3, 4, [5, 6], 7], 8]
}
```

### Output

```javascript
{
	"result":[1, 2, 3, 4, 5, 6, 7, 8]
}
```

### Extra point

- Optionally save the result
- Containerize 

## Solution

In order to have the extra point I modify the input, by adding a "save" key, to decide if the result is going to be saved. Iff save equals 1, the query is going to be saved.

### Modified Input


```javascript
{
	"items":[1, 2, [3, 4, [5, 6], 7], 8],
	"save": 1
}
```

The app is containerized with Dockers and it uses the port 56733. To run the container, type the following on terminal.

```bash
sudo bash start.sh
```

Once the container is running, to use the app 

```bash
curl http://localhost:56733/flat_list -d '{"save":1,"items": [1, 2, [3, 4, [5, 6], 7], 8]}' -H 'Content-Type: application/json'
```

To show saved lists

```bash 
curl http://localhost:5000/show_saved
```