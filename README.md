# Guitarist-Toolbox API
_Currently down due to new OS setup. Will be up ASAP!_

This is the Guitarist-Toolbox API service.  I built this public API originally for a guitar song writing application idea, but I felt it would be useful to allow everyone to use it as well! 

## Table of contents:

- Getting All Entire Toolbox
- Getting Single Type of Tool
- Advanced Queries of Tools
- Acquiring Randomized Type of Tool (under contruction)
- Contributing

## API Documentation 

### Get Entire Toolbox

Returns entire toolbox of items from database in JSON format. 

#### Request

```http
https://Guitarist-Toolbox.herokudns.com/music-info/all
```

#### Response

```ts
   { 
	"Whole Toolbox": [
		{
			"Chord":string
		}, ...
		{
			"Scale": string
		}, ...
		{
			"Technique": string
			"Type": string
		}, ...
		{
			"Time Signature": string
			"Type": string
		}
	   ]
     }
```

### Get Single Type of Tool

Returns a column from the toolbox based in the following parameters. 

#### Parameters

| param    | type     | Description                                                  |
| :------- | :------- | :----------------------------------------------------------- |
| chord  | `String` | Filters based on chord progression        |
| scale | `String` | Filters based on scale       |
| technique    | `String`    | Filters based on guitar technique |
|  time  | `String`    | Filters based on time signature                 |

#### Request

```http
https://Guitarist-Toolbox.herokudns.com/music-info/music-info/chord
```

#### Response

```ts
		{
			"Chord":string
		}
```

### Advanced Queries of Tools

Some columns have more than one parameter that be selected. Currently technique and time signature have two extra option parameters for querying. Returns a column from the toolbox based in the following parameters. 

#### Parameters

| param    | type     | Description                                                  |
| :------- | :------- | :----------------------------------------------------------- |
| technique/tech_type/<type\>  | `String` | Filters based on technique type: electric, acoustic, both        |
| time/tech_type/<type\>  | `String` | Filters based on time signature type: common, compound, complex     |

#### Request

```http
https://Guitarist-Toolbox.herokudns.com/music-info/music-info/time/tech_type/<type>
```

#### Response

```ts
		{
			"Time Signature":string,
			"Type": string
		}
```
## Contributing

All feedback and contributions are welcome!
