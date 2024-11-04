{
	"info": {
		"_postman_id": "56820b6b-5025-4bb1-a01d-e399b31073b8",
		"name": "Mutant API",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "34377736"
	},
	"item": [
		{
			"name": "http://127.0.0.1:5000/mutant",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"dna\": [\"ATGCGA\", \"CAGTGC\", \"TTATGT\", \"AGAAGG\", \"CCCCTA\", \"TCACTG\"]\n}\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/mutant",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"mutant"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/stats",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"count_mutant_dna\": 40,\n  \"count_human_dna\": 100,\n  \"ratio\": 0.4\n}\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/stats",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"stats"
					]
				}
			},
			"response": []
		}
	]
}