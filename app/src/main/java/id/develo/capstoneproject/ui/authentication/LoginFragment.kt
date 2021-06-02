package id.develo.capstoneproject.ui.authentication

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.viewModels
import com.google.android.material.snackbar.Snackbar
import id.develo.capstoneproject.MainActivity
import id.develo.capstoneproject.R
import id.develo.capstoneproject.databinding.FragmentLoginBinding


class LoginFragment : Fragment() {

    private var _binding: FragmentLoginBinding? = null
    private val binding get() = _binding!!

    private val loginViewModel: LoginViewModel by viewModels()

//    private lateinit var inputEmail: String
//    private lateinit var inputPassword: String

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        // Inflate the layout for this fragment
        _binding = FragmentLoginBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setProgressBar()

        launchSnackBar()

        moveToHomeIfSuccess()

        binding.btnLogin.setOnClickListener {
            checkUserInDatabase()
        }

        binding.tvSignup.setOnClickListener {
            // Move to Register Page
            moveToRegister()
        }
    }

    private fun checkUserInDatabase() {
        if (binding.tfEmail.editText?.text!!.isEmpty()) {
            binding.tfEmail.error = "This field is required!"
            return
        } else {
            binding.tfEmail.error = null
        }
        if (binding.tfPassword.editText?.text!!.isEmpty()) {
            binding.tfPassword.error = "This field is required!"
            return
        } else {
            binding.tfPassword.error = null
        }

        val inputEmail = binding.tfEmail.editText?.text.toString()
        val inputPassword = binding.tfPassword.editText?.text.toString()
        loginViewModel.getUser(inputEmail, inputPassword)
    }

    private fun moveToRegister() {
        val mRegisterFragment = RegisterFragment()
        val mFragmentManager = parentFragmentManager
        mFragmentManager.beginTransaction().apply {
            setCustomAnimations(R.anim.slide_in, R.anim.fade_out, R.anim.fade_in, R.anim.slide_out)
            replace(
                R.id.frame_container,
                mRegisterFragment,
                RegisterFragment::class.java.simpleName
            )
            addToBackStack(null)
            commit()
        }
    }

    private fun moveToHomeIfSuccess() {
        loginViewModel.isSuccess.observe(requireActivity(), { success ->
            if (success) {
                Intent(activity, MainActivity::class.java).also {
                    startActivity(it)
                    parentFragmentManager.popBackStack()
                }
            }
        })
    }

    private fun launchSnackBar() {
        loginViewModel.snackbarText.observe(requireActivity(), {
            it.getContentIfNotHandled()?.let { snackbarText ->
                Snackbar.make(
                    requireActivity().window.decorView.rootView,
                    snackbarText,
                    Snackbar.LENGTH_LONG
                ).show()
            }
        })
    }

    private fun setProgressBar() {
        loginViewModel.isLoading.observe(requireActivity(), {
            binding.progressBar.visibility = if (it) View.VISIBLE else View.GONE
        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
