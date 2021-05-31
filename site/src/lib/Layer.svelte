<script>
	import { onMount } from "svelte";
	import { layers } from "$lib/stores.js";

	export let name;
	export let id;
	export let index;
	export let ingredients = [];

	$: current = $layers[index].ingredient;

	export function choose() {
		return ingredients[Math.floor(Math.random() * ingredients.length)];
	}

	function set() {
		$layers[index].ingredient = choose();
	}

	onMount(() => {
		set();
	});
</script>

<div class="layer" {id} data-index={index}>
	<label
		>{name}
		<select name="{id}-{index}">
			{#each ingredients as ingredient}
				<option selected={ingredient === current}>{ingredient.name}</option>
			{/each}
		</select>
	</label>
	<button on:click={set}>Choose</button>
	<button on:click={layers.remove(index)}>Remove</button>
</div>
