# Calculator
Calculator neuron for Kalliope

## Synopsis
Calculate simple operations

## Installation
```bash
kalliope install --git-url https://github.com/corus87/calculator-neuron
```

## Options

| Parameter   | Required | Choices                          |
|-------------|----------|---------------------------------|
| variable_1  | yes      | integer                         |
| variable_2  | yes      | integer                         |
| operator    | yes      | add, subtract, multiply, divide |


## Return values

| Name         | Description                                  | Type   | Sample |
|--------------|----------------------------------------------|--------|--------|
| solution     | Returns the solution of the given operation  | string | 5      |

## Notes
- Only one operation is possible.
- Not all STT engines return integers! 

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
          operator: "add"
          say_template: "The solution is {{ solution }}"

  - name: "calculate-subtract"
    signals:
      - order: "calculate {{ var1 }} - {{ var2 }}"
      - order: "calculate {{ var1 }} subtract with {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "subtract"
          say_template: "The solution is {{ solution }}"
  
  - name: "calculate-multiply"
    signals:
      - order: "calculate {{ var1 }} x {{ var2 }}"
      - order: "calculate {{ var1 }} multiply by {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "multiply"
          say_template: "The solution is {{ solution }}"
  
  - name: "calculate-divide"
    signals:
      - order: "calculate {{ var1 }} / {{ var2 }}"
      - order: "calculate {{ var1 }} divide by {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "divide"
          say_template: "The solution is {{ solution }}"
```




