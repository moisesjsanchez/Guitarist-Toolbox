# Guitarist-Toolbox API

This is the Guitarist-Toolbox API service.  I built this API originally for a guitar song writing application idea, but I felt it would be useful to allow fellow guitarist to use it as well! Down below is documentation for this API.

_Disclaimer: Loading times might be slow because the service is asleep by default and must waken up._

## Table of contents:

- Getting Entire Toolbox
- Getting Single Type of Tool
- Getting Type Of Tool Based on Subtype
- Getting Randomized Type of Tool
- Contributing

## API Documentation

### Getting Entire Toolbox

Gets entire toolbox of items from database in JSON format.

#### Request

```http
https://guitarist-toolbox.herokuapp.com/music-info/all
```

#### Response

```ts
	[
  		{
  			"Chords":string
  		}, ...
  		{
  			"Scales": string
  		}, ...
  		{
  			"Techniques": string
  			"Type": string
  		}, ...
  		{
  			"Time Signatures": string
  			"Type": string
  		}
	]
```

### Getting Single Type of Tool

Gets toolbox items from the database based on type.

#### Parameters

| param    | type     | Description                                                  |
| :------- | :------- | :----------------------------------------------------------- |
| chords  | `String` | Filters based on chord progression        |
| scales | `String` | Filters based on scale       |
| techniques    | `String`    | Filters based on guitar technique |
|  times  | `String`    | Filters based on time signature                 |

#### Request

```http
https://guitarist-toolbox.herokuapp.com/music-info/chords
```

#### Response

```ts
	{
		"Chord":string
	}
```

### Getting Specific Type Of Tool

Gets toolbox items by type and subtype parameters. Currently technique and time signature have two optional subtype parameters for querying.

#### Parameters

| param    | subtype     | Description                                                  |
| :------- | :------- | :----------------------------------------------------------- |
| techniques/<type\>  | `String` | Filters based on technique type: electric, acoustic, both        |
| times/<type\>  | `String` | Filters based on time signature type: common, compound, complex     |

#### Request

```http
https://guitarist-toolbox.herokuapp.com/music-info/times/<type>
```

#### Response

```ts
	{
		"Time Signature":string,
		"Type": string
	}
```

### Getting Randomized Type of Tool

Gets a single toolbox item based on type and random parameter.

#### Request

```http
https://guitarist-toolbox.herokuapp.com/music-info/techniques/random
```

#### Response

```ts
	{
		"Technique":string,
		"Type": string
	}
```


## Contributing

Please message anything that I might have missed or should add from any of the tools' sections. All feedback, and contributions are welcome!
