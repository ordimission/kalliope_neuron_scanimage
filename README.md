# Scanimage

## Synopsis

Neuron to scan image with SANE

## Installation

```bash
kalliope install --git-url https://github.com/Ultchad/kalliope_neuron_translate
```

## Options

| parameter | required | default | choices                                | comments                                                                         |
|-----------|----------|---------|----------------------------------------|----------------------------------------------------------------------------------|
| depth     | no       |    8    |                                        |  |
| mode      | no       |  "color"|                                        |     |
| imageUri  | yes      |         |                                        |                                                              |
| imageFormat  | no      |   "png"      |       

## Return Values

| Name     | Description           | Type   | sample          |
|----------|-----------------------|--------|-----------------|
| result   | Result of translation | string | "Buenas noches" |
|      |

## Synapses example with override voice parameter

```yml
- name: "scanimage-fr"
  signals:
    - order: "acquiers l image"
  neurons:
    - scanimage:
        image_uri: "/tmp/image.png"
       
        
```
