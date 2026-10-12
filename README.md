# SVG Fourier Drawing

A small experiment that rebuilds an SVG path using a truncated complex Fourier series. The script samples the first path in `Fourier.svg`, calculates its Fourier coefficients, and plots the original shape alongside its Fourier reconstruction.

## Setup

```bash
pip install svgpathtools svg.path matplotlib numpy
```

Place an SVG file named `Fourier.svg` in the project folder. The script currently uses the first path found in that file.

## Run

```bash
python forsvg.py
```

The script displays the original SVG and Fourier reconstruction, saves them as `svgdraw.png` and `fourdraw.png`, and then opens an animation that progressively traces the Fourier reconstruction.

## Tuning

- `n` controls the number of samples taken from the SVG path.
- `k` controls the number of Fourier orders used for the reconstruction. Higher values usually produce a closer match, at the cost of more computation.

This project is a visual exploration of how Fourier series can describe shapes as rotating complex exponentials.
