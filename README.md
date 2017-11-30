# Calculator
Simple calculator neuron for Kalliope
## Synopsis

Calculate simple operations

## Installation
```bash
kalliope install --git-url https://github.com/corus87/calculator-neuron
```

## Options

| Parameter   | Required | Choice  | Default | 
|-------------|----------|---------|---------|
| variable_1  | yes      | integer |         | 
| variable_2  | yes      | integer |         | 
| add         | yes      | boolean | False   | 
| subtract    | yes      | boolean | False   | 
| multiply    | yes      | boolean | False   | 
| divide      | yes      | boolean | False   | 

## Return values

| Name         | Description                                  | Type   | Sample |
|--------------|----------------------------------------------|--------|--------|
| Solution     | Returns the solution of the givven operation | string | 5      |

## Note
Only one operation is possible.

## Synapses example
```
  - name: "calculate-add"
    signals:
      - order: "calculate {{ var1 }} + {{ var2 }}"
      - order: "calculate {{ var1 }} add {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          add: True
          say_template: "The solution is {{ solution }}"

  - name: "calculate-subtract"
    signals:
      - order: "calculate {{ var1 }} - {{ var2 }}"
      - order: "calculate {{ var1 }} subtract with {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          subtract: True
          say_template: "The solution is {{ solution }}"
  
  - name: "calculate-multiply"
    signals:
      - order: "calculate {{ var1 }} x {{ var2 }}"
      - order: "calculate {{ var1 }} multiply by {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          multiply: True
          say_template: "The solution is {{ solution }}"
  
  - name: "calculate-divide"
    signals:
      - order: "calculate {{ var1 }} / {{ var2 }}"
      - order: "calculate {{ var1 }} divided by {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          divide: True
          say_template: "The solution is {{ solution }}"
```




