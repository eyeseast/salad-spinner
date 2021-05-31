<script>
	import { afterUpdate } from "svelte";
	import { layers } from "$lib/stores.js";

	export let name;
	export let id;
	export let index;
	export let ingredients = [];

	let select;

	$: current = $layers[index].ingredient;

	function choose() {
		return ingredients[Math.floor(Math.random() * ingredients.length)];
	}

	function set(ingredient) {
		if (!ingredient) ingredient = choose();
		$layers[index].ingredient = ingredient;
	}

	function onChange(e) {
		$layers[index].ingredient = ingredients.find(item => e.target.value === item.name);
	}

	afterUpdate(() => {
		select.value = current.name;
	});
</script>

<div class="layer" {id} data-index={index}>
	<label
		>{name}
		<select name={id} bind:this={select} on:input={onChange}>
			<option value="" />
			{#each ingredients as ingredient}
				<option selected={ingredient.id === current?.id} value={ingredient.name}
					>{ingredient.name}</option
				>
			{/each}
		</select>
	</label>
	<button on:click|preventDefault={e => set()}>Shuffle</button>
	<button on:click|preventDefault={e => layers.remove(index)}>Remove</button>
</div>

<style>
	.layer {
		display: flex;
		margin-bottom: 0.5em;
	}
</style>
