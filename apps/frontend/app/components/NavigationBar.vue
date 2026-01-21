<style scoped>
.active-link {
  color: white;
  text-shadow: 0 0 12px rgba(99,102,241,0.6);
}
</style>

<template>
  <nav class="w-full">
    <div class="px-4 py-4 fixed w-full z-50 glass rounded-b-lg">
      <div
        class="flex items-center justify-between"
      >

        <!-- Brand -->
        <NuxtLink
          to="/"
          class="flex items-center gap-3 text-lg font-semibold hover:scale-105 transition-all"
        >
          <span class="gradient-text">
            LLM Studio
          </span>
        </NuxtLink>

        <!-- Links -->
        <div
          class="hidden md:flex items-center gap-10
                 text-sm font-medium
                 text-(--text-soft)"
        >
          <NuxtLink
		  	v-for="link in links"
            :key="link.to"
            :to="link.to"
            class="
				hover:text-white
				hover:scale-105
				active:scale-95
				transition-all"
            active-class="active-link"
          >
            {{ link.label }}
          </NuxtLink>
        </div>

        <!-- CTA -->
        <NuxtLink
          to="/build"
          class="px-5 py-2.5 rounded-xl
                 bg-(--primary)
                 text-white text-sm font-semibold
                 hover:opacity-90
                 active:scale-95
                 transition"
        >
          Connect wallet
        </NuxtLink>

      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
	interface NavLink {
	to: string
	label: string
	}

	const links: NavLink[] = [
	{ to: '/', label: 'Home' },
	{ to: '/build', label: 'Build' },
	{ to: '/docs', label: 'Docs' },
	{ to: '/about', label: 'About' },
	]
</script>
