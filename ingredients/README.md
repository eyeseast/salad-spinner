# Ingredients

Let's get the best ingredients we can find and get out of their way. Add everything you want in a salad here.

- [Greens](greens.yml)
- [Vegetables](vegetables.yml)
- [Legumes](legumes.yml)
- [Dairy](dairy.yml)
- [Grains](grains.yml)
- [Proteins](proteins.yml)

Simple ingredients, like [greens](greens.yml), look like this:

```yml
name: Greens

ingredients:
  - Arugula
  - Baby spinach
  - Iceberg Lettuce
  - Romaine Lettuce
```

Nothing complicated. Lettuce doesn't need a recipe. Please add any leafy greens you might put in a salad. Other ingredients need a little more:

```yml
name: Grains

ingredients:
  - name: Barley
    allergies: [gluten]
  - Brown rice
  - name: Bulgar wheat
    allergies: [gluten]
  - name: Farro
    allergies: [gluten]
  - Quinoa
  - Wild rice
```

Some [grains](grains.yml) need to mark allergy information (gluten, in this case) so I'm using objects instead of strings. I'm also mixing in the simpler style, because quinoa is just quinoa.

For cases like [dairy](dairy.yml), where everything has the same allergy, we can mark it in one place:

```yml
name: Dairy
allergies: [dairy]

ingredients:
  - Cheddar
  - Goat cheese
  - Feta
  - Sour cream
```

Marking allergies will let others filter out what they can't eat.

## Dressings, etc

For anything that does need an actual recipe (like salad dressing), please add a markdown file, and list ingredients in the frontmatter. For example, here's a [basic vinaigrette](ingredients/dressings/basic-vinaigrette.md):

```md
---
name: Basic vinaigrette
ingredients:
  - Red wine vinegar
  - Olive oil
  - Dijon mustard
  - Salt
  - Black pepper
---

Combine vinegar, oil and mustard in a small bowl and whisk together until fully emulsified. Add salt and pepper to taste.
```
