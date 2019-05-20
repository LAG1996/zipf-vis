<template>
	<article>
		<span
			v-for="word in coloredText"
			v-bind:class="['f'+word[1]]"
		>{{word[0]}}</span>
	</article>
</template>

<script>
	export default {
		name: 'colored-doc',
		data: () => {
			return { 
				coloredText: [],
			}
		},
		props: {
			text: '',
		},
		created: function() {
			this.$props.text.forEach((el) => {
				el[0].replace('\n', '<br/>');

				this.coloredText.push(el);
			});
		},
	};
</script>

<style>
</style>
