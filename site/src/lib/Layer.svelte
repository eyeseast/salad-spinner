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
		if (current) {
			select.value = current?.name;
		} else {
			set();
		}
	});
</script>

<div class="layer row" id="{index}-{id}" data-index={index}>
	<label class="form-label" for="select-{index}-{id}">{name}</label>

	<div class="col">
		<select
			id="select-{index}-{id}"
			class="form-select"
			name={id}
			bind:this={select}
			on:input={onChange}
		>
			<option value="" />
			{#each ingredients as ingredient}
				<option selected={ingredient.id === current?.id} value={ingredient.name}
					>{ingredient.name}</option
				>
			{/each}
		</select>
	</div>
	<div class="buttons col">
		<button class="btn btn-secondary btn-sm" on:click|preventDefault={e => set()}
			>Shuffle</button
		>
		<button
			class="btn btn-secondary btn-sm"
			on:click|preventDefault={e => layers.remove(index)}>Remove</button
		>
	</div>
</div>

<style>
	.layer {
		margin-bottom: 1.5em;
	}
</style>
