<template>
  <div class="min-h-screen bg-linear-to-br from-slate-950 via-purple-950 to-slate-950">
    <!-- Animated background elements -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl animate-pulse" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse delay-1000" />
    </div>

    <!-- Navigation -->
    <NavigationBar />

    <!-- Main Content -->
    <main class="relative z-10 pt-20">
      <slot />
    </main>

    <!-- Footer (optional) -->
    <!-- <FooterBar v-if="!$route.meta.hideFooter" /> -->
  </div>
</template>

<script setup lang="ts">
// Layout can have shared logic here if needed
</script>