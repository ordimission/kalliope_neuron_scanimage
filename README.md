# Scanimage

## Synopsis

Neuron to scan image with SANE

## Installation

```bash
kalliope install --git-url https://github.com/ordimission/kalliope_neuron_scanimage
```

## Options

| parameter | required | default | choices                                | comments                                                                         |
|-----------|----------|---------|----------------------------------------|----------------------------------------------------------------------------------|
| depth     | no       |    16   |                                        |  |
| mode      | no       |  "color"|                                        |     |
| image     | yes      |         |                                        |                                                              |
| format    | no       |   "png" |       

## Return Values

| Name     | Description           | Type   | sample          |
|----------|-----------------------|--------|-----------------|
|     |

## Synapses example with override voice parameter

```yml
- name: "scanimage-fr"
  signals:
    - order: "acquiers l'image"
  neurons:
    - scanimage:
        image: "/tmp/image.png"
       
        
```
